from src.SETAFGraph import SETAFGraph
from src.SETAFReader import SETAFReader
from src.command.BaseDisplayGraphCommand import BaseDisplayGraphCommand


class DisplayGraphCommand(BaseDisplayGraphCommand):
    NAME = "display-graph"
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

        self._draw_nodes(
            graph,
            node_size=graph.node_sizes(),
            font_color="#EEEEEE"
        )
        self._show_graph()
