#!/usr/bin/env python3
import argparse

from src.command.DisplaySETAFCommand import DisplayGraphCommand
from src.command.DisplayStrongLabelingCommand import \
    DisplayStrongLabelingCommand
from src.command.utils import wrap_command


def _build_parser():
    parser = argparse.ArgumentParser(
        description="Collection of SETAF utilities"
    )
    subparsers = parser.add_subparsers(
        dest='subcommand', required=True
    )
    commands = (
        DisplayGraphCommand,
        DisplayStrongLabelingCommand,
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
