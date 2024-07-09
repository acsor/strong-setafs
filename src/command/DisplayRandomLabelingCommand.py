import argparse

import networkx
import matplotlib.pyplot as plt

from src.SETAFLabeling import SETAFLabeling
from src.SETAFReader import SETAFReader
from src.command.Command import Command

from src.SETAFGraph import SETAFGraph


class DisplayRandomLabelingCommand(Command):
    NAME = "display-rl"
    DESCRIPTION = """
    Reads a SETAF from a CCL file and displays it along with a random
    labeling.
    """

    def __init__(self, args):
        super().__init__(args)

    @classmethod
    def set_up_parser(cls, parser):
        parser.add_argument(
            "input_file",
            type=argparse.FileType('r'),
            help="Input file in CCL format to read the SETAF from"
        )

        return parser

    def __call__(self):
        graph = SETAFGraph(
            SETAFReader(self._args.input_file)()
        )
        labeling = SETAFLabeling.random_labeling(graph.setaf)

        if networkx.is_planar(graph):
            draw = networkx.draw_planar
        else:
            draw = networkx.draw_circular

        draw(
            graph,
            with_labels=True,
            node_color=graph.node_colors(labeling),
            node_size=600,
            labels=graph.display_labels,
            font_color="#FFFFFF",
        )
        plt.show()
