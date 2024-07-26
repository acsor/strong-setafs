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
            help="Layout with which to display the graph"
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

    def _draw_edges(self, graph, edge_color=dict(), **options):
        layout = self.LAYOUTS[self._args.layout]
        single_edges = tuple(
            (a, b) for (a, b) in graph.edges if (b, a) not in graph.edges
        )
        double_edges = tuple(
            (a, b) for (a, b) in graph.edges if (b, a) in graph.edges
        )

        networkx.draw_networkx_edges(
            graph,
            edgelist=single_edges,
            pos=layout(graph),
            arrows=True,
            edge_color=tuple(
                map(lambda e: edge_color.get(e, "k"), single_edges)
            ),
            node_size=graph.node_sizes(),
            **options
        )
        # The edges (a, b) for which (b, a) is also an edge will be
        # drawn with a slight arc. Unfortunately networkx does not
        # adopt this behavior by default.
        networkx.draw_networkx_edges(
            graph,
            edgelist=double_edges,
            pos=layout(graph),
            arrows=True,
            edge_color=tuple(
                map(lambda e: edge_color.get(e, "k"), double_edges)
            ),
            node_size=graph.node_sizes(),
            connectionstyle='arc3,rad=0.3',
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
