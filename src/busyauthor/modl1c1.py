from . import args_common, modl2c1

command_aliases = ["cmd"]


def add_subparsers(subparser):
    parser = subparser.add_parser(
        "command",
        help="command help",
        aliases=command_aliases,
    )

    parser.add_argument("--command-args", help="command arguments")
    args_common.add_common_args(parser)

    modl2c1.add_subparsers(parser)

    return parser


def dostuff(args):
    print("doing work in command")
