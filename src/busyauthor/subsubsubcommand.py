from . import args_common, subsubsubsubcommand


def add_arguments(parser):
    parser.add_argument("--subsubsubcommand-args", help="subsubsubcommand arguments")
    args_common.add_common_args(parser)


def add_subparsers(parser):
    subparsers = parser.add_subparsers(
        dest="subsubsubcommand", help="Available subcommands"
    )

    parser = subparsers.add_parser(
        "subsubsubcommand",
        help="subsubsubcommand help",
        aliases=["subsubsubcmd"],
    )

    subsubsubsubcommand.add_subparsers(parser)

    add_arguments(parser)

    return parser
