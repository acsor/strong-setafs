class SETAF:
    def __init__(self, attacks):
        self._attacks = tuple(attacks)

    @property
    def attacks(self):
        return self._attacks

    @property
    def arguments(self):
        return frozenset(
            a.arguments for a in self._attacks
        )

    def __eq__(self, other):
        if type(other) is not SETAF:
            return False

        for (a1, a2) in zip(self.attacks, other.attacks):
            if a1 != a2:
                return False

        return True
