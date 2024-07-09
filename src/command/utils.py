def wrap_command(command_class):
    def call(args):
        command = command_class(args)

        command()

    return call
