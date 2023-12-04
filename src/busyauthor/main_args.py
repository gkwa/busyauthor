import argparse

from busyauthor import __version__
from busyauthor import args_common as argsmod

parser = argparse.ArgumentParser(description="Just a Fibonacci demonstration")
argsmod.add_common_args(parser)


parser.add_argument(
    "--version",
    action="version",
    version=f"busyauthor {__version__}",
)

parser.add_argument(dest="n", help="n-th Fibonacci number", type=int, metavar="INT")
