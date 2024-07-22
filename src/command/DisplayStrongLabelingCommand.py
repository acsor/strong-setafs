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
            "--target", type=int, default=None,
            help="Argument that is supposed to be in the grounded extension"
        )

        return parser

    def __call__(self):
        setaf = SETAFReader(self._args.input_file)()
        graph = SETAFGraph(setaf)
        labelings = setaf.strongly_admissible_labeling(
            self._args.target
        )

        if labelings:
            labeling, mm_labeling = labelings

            if self._args.verbose:
                print(labeling)

            self._draw_nodes(
                graph,
                node_color=graph.node_colors(labeling),
                # This refers to the color of the border of nodes, not to edges!
                edgecolors=graph.node_edge_colors(labeling),
                linewidths=2,
            )
            self._draw_node_labels(
                graph,
                font_color="#FFFFFF",
            )
            self._draw_edges(
                graph,
                edge_color=graph.edge_colors(labeling),
                width=2,
            )
            self._draw_edge_labels(
                graph,
                edge_labels=graph.edge_labels(labeling)
            )
            self._show_graph()
        else:
            print(
                "Argument %d was not reached by the labeling process" %
                self._args.target
            )
