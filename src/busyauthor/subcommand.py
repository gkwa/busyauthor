from . import args_common, subsubcommand


def add_arguments(parser):
    parser.add_argument("--subcommand-args", help="subcommand arguments")
    args_common.add_common_args(parser)


def add_subparsers(parser):
    subparsers = parser.add_subparsers(dest="subcommand", help="Available subcommands")

    parser = subparsers.add_parser(
        "subcommand",
        help="subcommand help",
        aliases=["subcmd"],
    )

    add_arguments(parser)

    subsubcommand.add_subparsers(parser)

    return parser
