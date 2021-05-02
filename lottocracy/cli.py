from docopt import docopt

import lottocracy


class cli():
    """Lottocracy playground

    Usage:
        lottocracy [options] <command> [<args>...]

    Commands:
        facebook      Manage your lottocracy in a Facebook group

    Options:
        -h --help     Show this screen.
        --version     Show version.
    """

    def __init__(self):
        pass

    def execute(self):
        args = docopt(self.__class__.__doc__, version=lottocracy.__meta__.version, options_first=True)
        command_args = [args['<command>']] + args['<args>']
        if args['<command>'] == 'facebook':
            from . import cli_facebook
            cli_facebook.Facebook().execute(command_args)


def main():
    cli().execute()


if __name__ == '__main__':
    main()
