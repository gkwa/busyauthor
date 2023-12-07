import argparse
import logging
import sys

from . import (
    __version__,
    args_common,
    modl1c1,
    modl1c2,
    modl1c3,
    modl2c1,
    modl3c1,
    modl4c1,
    modl5c1,
)


def setup_logging(loglevel=None, logger=None):
    """Setup basic logging

    Args:
        loglevel (Optional[int]): minimum loglevel for emitting messages, defaults to None.   # noqa: E501
        logger (Optional[logging.Logger]): Logger instance, defaults to None.
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(logformat, datefmt="%Y-%m-%d %H:%M:%S"))

    if logger is None:
        logger = logging.getLogger(__name__)

    if loglevel is not None:
        logger.setLevel(loglevel)
    else:
        logger.setLevel(logging.WARN)

    logger.addHandler(handler)


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

subparser = parser.add_subparsers(dest="command", help="Available commands")

# Add top level commands here
modl1c1.add_subparsers(subparser)
modl1c2.add_subparsers(subparser)
modl1c3.add_subparsers(subparser)


def main(args):
    args = parser.parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    db_file = args.db  # noqa: F841

    cmd = getattr(args, "command", None)

    if cmd == "command3" or cmd in modl1c3.command_aliases:
        modl1c3.dostuff(args)

    if cmd == "command2" or cmd in modl1c2.command_aliases:
        modl1c2.dostuff(args)

    if cmd == "command" or cmd in modl1c1.command_aliases:
        modl1c1.dostuff(args)

        cmd = getattr(args, "subcommand", None)

        if cmd == "subcommand" or cmd in modl2c1.command_aliases:
            modl2c1.dostuff(args)

            cmd = getattr(args, "subsubcommand", None)

            if cmd == "subsubcommand" or cmd in modl3c1.command_aliases:
                modl3c1.dostuff(args)

                cmd = getattr(args, "subsubsubcommand", None)

                if cmd == "subsubsubcommand" or cmd in modl4c1.command_aliases:
                    modl4c1.dostuff2(args)
                    modl4c1.dostuff()

                    cmd = getattr(args, "subsubsubsubcommand", None)

                    if cmd == "subsubsubcommand" or cmd in modl5c1.command_aliases:
                        modl5c1.dostuff(args)

    _logger.info("Script ends here")


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
