class SETAF:
    def __init__(self, attacks):
        self._attacks = attacks

    @property
    def attacks(self):
        return self._attacks