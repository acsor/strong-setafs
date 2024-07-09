#!/usr/bin/env python3
import argparse

from src.command.DisplayGraphCommand import DisplayGraphCommand
from src.command.wrap_command import wrap_command


def _build_parser():
    parser = argparse.ArgumentParser(
        description="Collection of SETAF utilities"
    )
    subparsers = parser.add_subparsers(
        dest='subcommand', required=True
    )
    commands = (
        DisplayGraphCommand,
    )

    for c in commands:
        p = c.set_up_parser(
            subparsers.add_parser(
                c.NAME,
                description=c.DESCRIPTION
            )
        )
        p.set_defaults(
            func=wrap_command(c)
        )

    return parser


def main():
    parser = _build_parser()
    args = parser.parse_args()

    return args.func(args)


if __name__ == "__main__":
    exit(main())
