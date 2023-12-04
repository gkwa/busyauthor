import argparse

from busyauthor import __version__, args_common

parser = argparse.ArgumentParser(
    description="Just a command, sub command, subsub command demonstration"
)
args_common.add_common_args(parser)


parser.add_argument(
    "--version",
    action="version",
    version=f"busyauthor {__version__}",
)
parser.add_argument("--db", help="Specify the database file (e.g., data.cypher)")
