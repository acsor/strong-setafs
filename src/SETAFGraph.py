import networkx

class SETAFGraph(networkx.DiGraph):
    def __init__(self, setaf):
        super().__init__()
        self._setaf = setaf
        self._display_labels = dict()

        for a in setaf.attacks:
            self.add_node(a.attackers)
            self.add_node(a.attacked)

            self._display_labels[a.attackers] = "{%s}" % ",".join(
                map(str, a.attackers)
            )
            self._display_labels[a.attacked] = str(a.attacked)

            self.add_edge(a.attackers, a.attacked)

    @property
    def display_labels(self):
        return self._display_labels