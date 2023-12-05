from . import args_common, level2


def add_arguments(parser):
    parser.add_argument("--command-args", help="command arguments")
    args_common.add_common_args(parser)


def add_subparsers(parser):
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    parser = subparsers.add_parser(
        "command",
        help="command help",
        aliases=["cmd"],
    )
    add_arguments(parser)

    level2.add_subparsers(parser)

    return parser
