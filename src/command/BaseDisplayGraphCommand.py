import argparse

import networkx
from matplotlib import pyplot as plt

from src.command.Command import Command


class BaseDisplayGraphCommand(Command):
    LAYOUTS = {
        # "bipartite": networkx.bipartite_layout,
        # "bfs": networkx.bfs_layout,
        "circular": networkx.circular_layout,
        "kamada_kawai": networkx.kamada_kawai_layout,
        "planar": networkx.planar_layout,
        "random": networkx.random_layout,
        "shell": networkx.shell_layout,
        "spring": networkx.spring_layout,
        "spectral": networkx.spectral_layout,
        "spiral": networkx.spiral_layout,
    }

    @classmethod
    def set_up_parser(cls, parser):
        parser = super().set_up_parser(parser)

        parser.add_argument(
            "--layout",
            choices=tuple(cls.LAYOUTS.keys()),
            default="circular",
            help="Layout to display the graph vertices with"
        )
        parser.add_argument(
            "input_file",
            type=argparse.FileType('r'),
            help="Input file in CCL format to read the SETAF from"
        )

        return parser

    def _draw_nodes(self, graph, **options):
        layout = self.LAYOUTS[self._args.layout]

        networkx.draw_networkx_nodes(
            graph,
            pos=layout(graph),
            node_size=graph.node_sizes(),
            node_shape="o",
            **options
        )

    def _draw_node_labels(self, graph, **options):
        layout = self.LAYOUTS[self._args.layout]

        networkx.draw_networkx_labels(
            graph,
            pos=layout(graph),
            labels=graph.node_labels(),
            **options
        )

    def _draw_edges(self, graph, **options):
        layout = self.LAYOUTS[self._args.layout]

        networkx.draw_networkx_edges(
            graph,
            pos=layout(graph),
            arrows=True,
            node_size=graph.node_sizes(),
            **options
        )

    def _draw_edge_labels(self, graph, **options):
        layout = self.LAYOUTS[self._args.layout]

        networkx.draw_networkx_edge_labels(
            graph,
            pos=layout(graph),
            font_size=12,
            **options
        )

    def _show_graph(self):
        plt.show()
