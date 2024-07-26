import networkx
from colour import Color

from src.Attack import Attack
from src.SETAFLabeling import Label


class SETAFGraph(networkx.DiGraph):
    NODE_COLORS = {
        Label.IN: Color("green", luminance=0.3).hex,
        Label.OUT: Color("red", luminance=0.45).hex,
        Label.UNDEC: Color("gray", luminance=0.6).hex
    }
    NODE_EDGE_COLORS = {
        Label.IN: NODE_COLORS[Label.IN],
        Label.OUT: NODE_COLORS[Label.OUT],
        Label.UNDEC: NODE_COLORS[Label.UNDEC],
    }
    EDGE_COLORS = {
        Label.IN: Color("red", luminance=0.45).hex,
        Label.OUT: Color("gray", luminance=0.6).hex,
        Label.UNDEC: Color("gray", luminance=0.6).hex
    }

    def __init__(self, setaf):
        super().__init__()
        self._setaf = setaf
        self._node_labels = dict()

        for a in setaf.arguments:
            self.add_node(a)
            self._node_labels[a] = str(a)

        for a in setaf.attacks:
            # Add an explicit vertex for an attack only if this attack
            # contains more than one attacker.
            if len(a.attackers) > 1:
                self.add_node(a)
                self._node_labels[a] = ""
                self.add_edge(a, a.attacked)
            # Otherwise, just add a vertex from the already existing
            # attacker to the already existing attacked argument.
            elif len(a.attackers) == 1:
                self.add_edge(
                    tuple(a.attackers)[0], a.attacked
                )
            else:
                raise Exception("Invalid number of arguments")

    @staticmethod
    def _simple_edge_label(edge):
        attack, attacked = edge

        if type(attack) is Attack:
            return ", ".join(
                map(lambda x: "%s" % x, attack.attackers)
            )
        elif type(attack) is int:
            return ""
        else:
            raise ValueError(
                "%s is an unrecognized vertex type" % type(attack)
            )

    @staticmethod
    def _enhanced_edge_label(edge, labeling):
        attack, attacked = edge

        if type(attack) is Attack:
            sign = {
                Label.IN: "+",
                Label.OUT: "-",
                Label.UNDEC: "?"
            }

            return ", ".join(
                map(
                    lambda x: "%s%s" % (sign[labeling[x]], x),
                    attack.attackers
                )
            )
        elif type(attack) is int:
            return ""
        else:
            raise ValueError(
                "%s is an unrecognized vertex type" % type(attack)
            )

    @property
    def setaf(self):
        return self._setaf

    def node_colors(self, labeling):
        """
        :param labeling: An instance of SETAFLabeling.
        """
        # TODO Rename method.
        return tuple(
            map(
                lambda n: self.NODE_COLORS[labeling[n]], self.nodes
            )
        )

    def node_edge_colors(self, labeling):
        """
        :param labeling: An instance of SETAFLabeling.
        """
        return tuple(
            map(
                lambda n: self.NODE_EDGE_COLORS[labeling[n]], self.nodes
            )
        )

    def node_labels(self):
        return self._node_labels

    def edge_labels(self, labeling=None):
        """
        :return: A dictionary having edges as keys and a string representing
        the edge label as value. If `labeling` is specified, additional
        information specified by `labeling` will be displayed on the edge label.
        """
        if labeling:
            return {
                edge: self._enhanced_edge_label(edge, labeling) for edge in
                self.edges
            }
        else:
            return {
                edge: self._simple_edge_label(edge) for edge in self.edges
            }

    def edge_colors(self, labeling):
        return {
            e: self.EDGE_COLORS[labeling[e[0]]] for e in self.edges
        }

    def node_sizes(self):
        return tuple(
            map(
                lambda n: 100 if type(n) is Attack else 600, self.nodes
            )
        )
