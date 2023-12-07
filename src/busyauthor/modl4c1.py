from . import args_common, modl5c1

command_aliases = ["subsubsubcmd"]


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
        aliases=command_aliases,
    )

    modl5c1.add_subparsers(parser)

    add_arguments(parser)

    return parser


def dostuff():
    print("doing work in subsubsubcommand")


def dostuff2(args):
    print(f"{args.subsubsubcommand_args=}")
