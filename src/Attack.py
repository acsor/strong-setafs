class Attack:
    def __init__(self, attackers, attacked):
        self._attackers = frozenset(attackers)
        self._attacked = attacked

    @property
    def attackers(self):
        return self._attackers

    @property
    def attacked(self):
        return self._attacked

    @property
    def arguments(self):
        """
        :return: A frozenset of all attackers and attacked arguments
        contained in this attack.
        """
        return self._attackers | frozenset((self._attacked, ))

    def __eq__(self, other):
        return type(other) is Attack and\
            self.attackers == other.attackers and \
            self.attacked == other.attacked
