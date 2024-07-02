class Attack:
    def __init__(self, attackers, attacked):
        self._attackers = attackers
        self._attacked = attacked

    @property
    def attackers(self):
        return self._attackers

    @property
    def attacked(self):
        return self._attacked
