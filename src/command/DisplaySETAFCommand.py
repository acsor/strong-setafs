from src.SETAFGraph import SETAFGraph
from src.SETAFReader import SETAFReader
from src.command.BaseDisplayGraphCommand import BaseDisplayGraphCommand


class DisplayGraphCommand(BaseDisplayGraphCommand):
    NAME = "display-setaf"
    DESCRIPTION = """
    Reads a SETAF from a CCL file and displays it on a window.
    """

    def __init__(self, args):
        super().__init__(args)

    @classmethod
    def set_up_parser(cls, parser):
        parser = super().set_up_parser(parser)

        return parser

    def __call__(self):
        graph = SETAFGraph(
            SETAFReader(self._args.input_file)()
        )

        self._draw_nodes(graph)
        self._draw_node_labels(
            graph,
            font_color="#FFFFFF",
        )
        self._draw_edges(graph)
        self._draw_edge_labels(
            graph,
            edge_labels=graph.edge_labels()
        )
        self._show_graph()
