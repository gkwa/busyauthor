from . import args_common, level4


def add_arguments(parser):
    parser.add_argument("--subsubcommand-args", help="subsubcommand arguments")
    args_common.add_common_args(parser)


def add_subparsers(parser):
    subparsers = parser.add_subparsers(
        dest="subsubcommand", help="Available subcommands"
    )

    parser = subparsers.add_parser(
        "subsubcommand",
        help="subsubcommand help",
        aliases=["subsubcmd"],
    )

    level4.add_subparsers(parser)

    add_arguments(parser)

    return parser


def dostuff():
    print("doing work")
