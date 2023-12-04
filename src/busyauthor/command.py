import argparse

from busyauthor import args_common as argsmod

parser = argparse.ArgumentParser(description="command parser")
argsmod.add_common_args(parser)


subparsers = parser.add_subparsers(
    description="valid commands",
    title="command",
    help="command help",
    required=True,
    dest="command",
)

command_parser = subparsers.add_parser(
    "command", aliases=["cmd"], help="Top-level command"
)

command_parser.add_argument("--command-args", help="Arguments for the command")
