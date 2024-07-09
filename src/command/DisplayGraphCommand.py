import argparse

import networkx
import matplotlib.pyplot as plt

from src.SETAFReader import SETAFReader
from src.command.Command import Command

from src.SETAFGraph import SETAFGraph


class DisplayGraphCommand(Command):
    NAME = "display-graph"
    DESCRIPTION = """
    Reads a SETAF from a CCL file and writes its graph
    conversion to an output file.
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

        if networkx.is_planar(graph):
            draw = networkx.draw_planar
        else:
            draw = networkx.draw_circular

        draw(
            graph,
            with_labels=True,
            node_color="#A3A3A3",
            node_size=600,
            labels=graph.display_labels,
            font_color="#FFFFFF",
        )
        plt.show()
