import argparse

from busyauthor import __version__
from busyauthor import args_common as argsmod

parser = argparse.ArgumentParser(
    description="Just a command, sub command, subsub command demonstration"
)
argsmod.add_common_args(parser)


parser.add_argument(
    "--version",
    action="version",
    version=f"busyauthor {__version__}",
)
