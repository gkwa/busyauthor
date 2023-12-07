from . import args_common

command_aliases = ["cmd3"]


def add_subparsers(subparser):
    parser = subparser.add_parser(
        "command3",
        help="command3 help",
        aliases=["cmd3"],
    )

    parser.add_argument("--command3-args", help="command arguments")
    args_common.add_common_args(parser)

    return parser


def dostuff(args):
    print(args)
    print("doing work in command3")
