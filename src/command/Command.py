class Command:
    def __init__(self, args):
        self._args = args

    def set_up_parser(self, parser):
        raise NotImplemented()
