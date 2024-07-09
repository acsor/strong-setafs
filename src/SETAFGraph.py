import networkx

from src.SETAFLabeling import Label


class SETAFGraph(networkx.DiGraph):
    def __init__(self, setaf):
        super().__init__()
        self._setaf = setaf
        self._display_labels = dict()

        for a in setaf.attacks:
            self.add_node(a)
            self.add_node(a.attacked)

            self._display_labels[a] = "{%s}" % ",".join(
                map(str, a.attackers)
            )
            self._display_labels[a.attacked] = str(a.attacked)

            self.add_edge(a, a.attacked)

    @property
    def setaf(self):
        return self._setaf

    def node_colors(self, labeling):
        colors = {
            Label.IN: '#008000',
            Label.OUT: '#FF0000',
            Label.UNDEC: '#A9A9A9'
        }

        return tuple(
            map(
                lambda n: colors[labeling[n]], self.nodes
            )
        )

    @property
    def display_labels(self):
        return self._display_labels
