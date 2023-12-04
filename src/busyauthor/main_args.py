import argparse

from busyauthor import __version__
from busyauthor import args_common as argsmod
from busyauthor import command

parser = argparse.ArgumentParser(
    description="Just a command, sub command, subsub command demonstration"
)
argsmod.add_common_args(parser)


def add_arguments(parser):
    parser.add_argument(
        "--version",
        action="version",
        version=f"busyauthor {__version__}",
    )
    parser.add_argument("--db", help="Specify the database file (e.g., data.cypher)")


def add_parser(subparsers):
    parser = subparsers.add_parser(
        "down",
        help=(
            "download url and expand (if zip) into cwd.  Example: {cmd} down "
            "https://www.dropbox.com/s/zirk55k8ty0dy1i/Spectra.prm.2.0.4.zip?dl=0"
        ),
    )
    add_arguments(parser)


add_arguments(parser)
add_parser(command.subparsers)
