import argparse


class DisplayGraphCommand:
    NAME = "display-graph"
    DESCRIPTION = """
    Reads a SETAF from a CCL file and writes its graph
    conversion to an output file.
    """

    @classmethod
    def set_up_parser(cls, parser):
        parser.add_argument(
            "file",
            type=argparse.FileType('r'),
            help="Input file in CCL format to read the SETAF from"
        )

    @classmethod
    def call(cls):
        print("Hello world")
