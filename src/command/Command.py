class Command:
    def __init__(self, args):
        self._args = args

    @classmethod
    def set_up_parser(self, parser):
        parser.add_argument(
            '-v', '--verbose', action='store_true',
            help='Display additional information'
        )

        return parser