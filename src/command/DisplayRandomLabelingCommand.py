import argparse

import matplotlib.pyplot as plt
import networkx

from src.SETAFGraph import SETAFGraph
from src.SETAFLabeling import SETAFLabeling
from src.SETAFReader import SETAFReader
from src.command.BaseDisplayGraphCommand import BaseDisplayGraphCommand


class DisplayRandomLabelingCommand(BaseDisplayGraphCommand):
    NAME = "display-rl"
    DESCRIPTION = """
    Reads a SETAF from a CCL file and displays it along with a random
    labeling.
    """

    def __init__(self, args):
        super().__init__(args)

    @classmethod
    def set_up_parser(cls, parser):
        parser = super().set_up_parser(parser)

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
        layout = self.LAYOUTS[
            self._args.layout
        ]

        networkx.draw(
            graph,
            pos=layout(graph),
            with_labels=True,
            node_color=graph.node_colors(labeling),
            node_size=600,
            labels=graph.display_labels,
            font_color="#FFFFFF",
        )
        plt.show()
