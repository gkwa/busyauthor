from . import args_common, modl3c1

command_aliases = ["subcmd"]


def add_arguments(parser):
    parser.add_argument("--subcommand-args", help="subcommand arguments")
    args_common.add_common_args(parser)


def add_subparsers(parser):
    subparsers = parser.add_subparsers(dest="subcommand", help="Available subcommands")

    parser = subparsers.add_parser(
        "subcommand",
        help="subcommand help",
        aliases=command_aliases,
    )

    add_arguments(parser)

    modl3c1.add_subparsers(parser)

    return parser


def dostuff(args):
    print("doing work in subcommand")
