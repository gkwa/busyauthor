from . import args_common


def add_arguments(parser):
    parser.add_argument("--command2-args", help="command2 arguments")
    args_common.add_common_args(parser)


def add_subparsers(parser):
    subparsers = parser.add_subparsers(dest="command2", help="Available commands")

    parser = subparsers.add_parser(
        "command2",
        help="command2 help",
        aliases=["cmd2"],
    )
    add_arguments(parser)

    return parser
