from . import args_common

command_aliases = ["cmd2"]


def add_subparsers(subparser):
    parser = subparser.add_parser(
        "command2",
        help="command2 help",
        aliases=["cmd2"],
    )

    parser.add_argument("--command2-args", help="command arguments")
    args_common.add_common_args(parser)

    return parser


def dostuff(args):
    print("doing work in command2")
