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
            # Add an explicit node for an attack only if this attack
            # contains more than one attacker.
            if len(a.attackers) > 1:
                self.add_node(a)
                self._node_labels[a] = ""
                self.add_edge(a, a.attacked)
                self._edge_labels[(a, a.attacked)] = ", ".join(
                    map(str, a.attackers)
                )
            # Otherwise, just add a vertex from the already existing
            # attacker to the already existing attacked argument.
            elif len(a.attackers) == 1:
                self.add_edge(
                    tuple(a.attackers)[0], a.attacked
                )
            else:
                raise Exception("Invalid number of arguments")

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
