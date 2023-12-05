import argparse
import logging
import sys

from . import __version__, args_common, level1, level2, utils


def setup_logging(loglevel):
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


__author__ = "Taylor Monacelli"
__copyright__ = "Taylor Monacelli"
__license__ = "MPL-2.0"

_logger = logging.getLogger(__name__)


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

level1.add_subparsers(parser)


def main(args):
    args = parser.parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    utils.print_command_hierarchy(args)
    db_file = args.db

    command = getattr(args, "command", None)
    command_args = getattr(args, "command_args", None)

    command2 = getattr(args, "command2", None)
    command2_args = getattr(args, "command2_args", None)

    subcommand = getattr(args, "subcommand", None)
    subcommand_args = getattr(args, "subcommand_args", None)

    subsubcommand = getattr(args, "subsubcommand", None)
    subsubcommand_args = getattr(args, "subsubcommand_args", None)

    subsubsubcommand = getattr(args, "subsubsubcommand", None)
    subsubsubcommand_args = getattr(args, "subsubsubcommand_args", None)

    subsubsubsubcommand = getattr(args, "subsubsubsubcommand", None)
    subsubsubsubcommand_args = getattr(args, "subsubsubsubcommand_args", None)

    if command:
        level1.dostuff()

        if subcommand:
            level2.dostuff()

    _logger.info("Script ends here")


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
