from . import args_common


def add_arguments(parser):
    parser.add_argument(
        "--subsubsubsubcommand-args", help="subsubsubsubcommand arguments"
    )
    args_common.add_common_args(parser)


def add_subparsers(parser):
    subparsers = parser.add_subparsers(
        dest="subsubsubsubcommand", help="Available subcommands"
    )

    parser = subparsers.add_parser(
        "subsubsubsubcommand",
        help="subsubsubsubcommand help",
        aliases=["subsubsubsubcmd"],
    )

    add_arguments(parser)

    return parser
