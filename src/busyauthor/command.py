from busyauthor import main_args as argsmod


def add_arguments(parser):
    parser.add_argument("--command-args", help="command args")


def add_parser(subparsers):
    parser = subparsers.add_parser(
        "command",
        help="Top-level command",
    )
    add_arguments(parser)


add_parser(argsmod.subparsers)
