from src.SETAFLabeling import Label, SETAFLabeling


class SETAF:
    def __init__(self, attacks):
        self._attacks = tuple(attacks)

    @property
    def attacks(self):
        return self._attacks

    @property
    def arguments(self):
        return frozenset.union(
            *(a.arguments for a in self._attacks)
        )

    def strongly_admissible_labeling(self, target):
        """
        Implements a generalization of the strong labeling algorithm for
        ordinary AFs introduced by Caminada and Harikrishnan for SETAFs.
        :param target: Argument that is assumed to belong to the grounded
        extension.
        :return: A pair composed of an admissible labeling and a min-max
        numbering, or `None` if `target` is never hit by the labeling process.
        """
        if target not in self.arguments:
            raise ValueError(
                "target argument is supposed to belong to the SETAF"
            )

        labeling = SETAFLabeling(self)
        mm_labeling = dict()
        attacks, attacks_count = list(), dict()

        for a in self.arguments:
            labeling[a] = Label.UNDEC
            attacks_count[a] = self.attacks_count(a)

            if attacks_count[a] == 0:
                labeling[a] = Label.IN
                mm_labeling[a] = 1

        for attack in self.attacks:
            labeling[attack] = Label.UNDEC

            if labeling[*attack.attackers] == Label.IN:
                labeling[attack] = Label.IN
                mm_labeling[attack] = 1
                attacks.append(attack)

        if labeling[target] == Label.IN:
            return (labeling, mm_labeling)

        while attacks:
            # Retrieve the next in-labeled attack
            attack = attacks.pop(0)
            attacked = attack.attacked

            # Label the argument attacked by `attack` out.
            # `attack` is in, so attacked must be out.
            labeling[attacked] = Label.OUT
            mm_labeling[attacked] = mm_labeling[attack] + 1

            # Since `attacked` is now out, some attacks might be rendered
            # out as well. Initiate a labeling procedure for them.
            for out_attack in filter(
                lambda x: attacked in x.attackers,
                self.attacks
            ):
                labeling[out_attack] = Label.OUT
                mm_labeling[out_attack] = mm_labeling[attacked]

                # `out_attack` is out, so the argument it attacks
                # has one fewer attacker.
                attacks_count[out_attack.attacked] -= 1

                if attacks_count[out_attack.attacked] == 0:
                    labeling[out_attack.attacked] = Label.IN
                    mm_labeling[out_attack.attacked] = mm_labeling[
                        out_attack
                    ] + 1

            for undec_attack in filter(
                lambda x: labeling[x] == Label.UNDEC,
                self.attacks
            ):
                if labeling[*undec_attack.attackers] == Label.IN:
                    labeling[undec_attack] = Label.IN
                    mm_labeling[undec_attack] = max(
                        mm_labeling[x] for x in undec_attack.attackers
                    )
                    attacks.append(undec_attack)

            if labeling[target] == Label.IN:
                break

        if labeling[target] != Label.IN:
            return None

        return (labeling, mm_labeling)

    def attacks_count(self, argument):
        """
        :return: The number of attacks targeting `argument`.
        """
        return sum(
            1 for attack in self.attacks if attack.attacked == argument
        )

    def __eq__(self, other):
        if type(other) is not SETAF:
            return False

        for (a1, a2) in zip(self.attacks, other.attacks):
            if a1 != a2:
                return False

        return True
