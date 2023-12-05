from . import args_common, level2


def add_subparsers(parser):
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    parser = subparsers.add_parser(
        "command",
        help="command help",
        aliases=["cmd"],
    )

    parser.add_argument("--command-args", help="command arguments")
    args_common.add_common_args(parser)

    level2.add_subparsers(parser)

    parser = subparsers.add_parser(
        "command2",
        help="command2 help",
        aliases=["cmd2"],
    )

    parser.add_argument("--command2-args", help="command2 arguments")
    args_common.add_common_args(parser)

    return parser


def dostuff():
    print("doing work")
