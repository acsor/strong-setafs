import networkx
from matplotlib import pyplot as plt

from src.SETAFGraph import SETAFGraph
from src.SETAFReader import SETAFReader
from src.command.BaseDisplayGraphCommand import BaseDisplayGraphCommand


class DisplayStrongLabelingCommand(BaseDisplayGraphCommand):
    NAME = "display-sl"
    DESCRIPTION = """
    Displays the strongly admissible labeling of the input graph.
    """

    def __init__(self, args):
        super().__init__(args)

    @classmethod
    def set_up_parser(cls, parser):
        parser = super().set_up_parser(parser)

        parser.add_argument(
            "target", type=int,
            help="Argument that is supposed to be in the grounded extension"
        )

        return parser

    def __call__(self):
        setaf = SETAFReader(self._args.input_file)()
        graph = SETAFGraph(setaf)
        labelings = setaf.strongly_admissible_labeling(
            self._args.target
        )
        layout = self.LAYOUTS[self._args.layout]

        if labelings:
            labeling, mm_labeling = labelings

            if self._args.verbose:
                print(labeling)

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
        else:
            print(
                "Argument %d was not reached by the labeling process" %
                self._args.target
            )
