import networkx

from src.Attack import Attack
from src.SETAFLabeling import Label


class SETAFGraph(networkx.DiGraph):
    def __init__(self, setaf):
        super().__init__()
        self._setaf = setaf
        self._node_labels = dict()
        self._edge_labels = dict()

        for a in setaf.arguments:
            self.add_node(a)
            self._node_labels[a] = str(a)

        for a in setaf.attacks:
            self.add_node(a)
            self.add_edge(a, a.attacked)

            self._node_labels[a] = ""
            self._edge_labels[(a, a.attacked)] = "%s" % ", ".join(
                map(str, a.attackers)
            )

    @property
    def setaf(self):
        return self._setaf

    def node_colors(self, labeling):
        """
        :param labeling: An instance of SETAFLabeling.
        """
        # TODO Rename method.
        colors = {
            Label.IN: '#38CF4A',
            Label.OUT: '#FF7A72',
            Label.UNDEC: '#C3C3C3'
        }

        return tuple(
            map(
                lambda n: colors[labeling[n]], self.nodes
            )
        )

    def node_edge_colors(self, labeling):
        """
        :param labeling: An instance of SETAFLabeling.
        """
        colors = {
            Label.IN: '#239930',
            Label.OUT: '#E63B31',
            Label.UNDEC: '#999999'
        }

        return tuple(
            map(
                lambda n: colors[labeling[n]], self.nodes
            )
        )

    def node_labels(self):
        return self._node_labels

    def edge_labels(self):
        return self._edge_labels

    def edge_colors(self, labeling):
        colors = {
            Label.IN: '#FF7A72',
            Label.OUT: '#C3C3C3',
            Label.UNDEC: '#C3C3C3'
        }

        return tuple(
            map(
                lambda e: colors[labeling[e[0]]], self.edges
            )
        )

    def node_sizes(self):
        return tuple(
            map(
                lambda n: 100 if type(n) is Attack else 600, self.nodes
            )
        )

