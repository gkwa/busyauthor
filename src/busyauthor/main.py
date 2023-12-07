import argparse
import logging
import sys

from . import (
    __version__,
    args_common,
    module_a1,
    module_a2,
    module_aa,
    module_aaa,
    module_aaaa,
    module_aaaaa,
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

module_a1.add_subparsers(subparser)
module_a2.add_subparsers(subparser)


def main(args):
    args = parser.parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    db_file = args.db  # noqa: F841

    cmd = getattr(args, "command", None)

    if cmd == "command2" or cmd in module_a2.command_aliases:
        module_a2.dostuff(args)

    if cmd == "command" or cmd in module_a1.command_aliases:
        module_a1.dostuff(args)

        cmd = getattr(args, "subcommand", None)

        if cmd == "subcommand" or cmd in module_aa.command_aliases:
            module_aa.dostuff(args)

            cmd = getattr(args, "subsubcommand", None)

            if cmd == "subsubcommand" or cmd in module_aaa.command_aliases:
                module_aaa.dostuff(args)

                cmd = getattr(args, "subsubsubcommand", None)

                if cmd == "subsubsubcommand" or cmd in module_aaaa.command_aliases:
                    module_aaaa.dostuff2(args)
                    module_aaaa.dostuff()

                    cmd = getattr(args, "subsubsubsubcommand", None)

                    if cmd == "subsubsubcommand" or cmd in module_aaaaa.command_aliases:
                        module_aaaaa.dostuff(args)

    _logger.info("Script ends here")


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
