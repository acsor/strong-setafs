import argparse

import networkx

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
