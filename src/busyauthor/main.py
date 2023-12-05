import argparse
import logging
import sys

from . import __version__, args_common, level2, level3, level4, module_a, module_b


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

module_a.add_subparsers(parser)


def main(args):
    args = parser.parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    db_file = args.db  # noqa: F841

    command = getattr(args, "command", None)

    if command:
        command_args = getattr(args, "command_args", None)  # noqa: F841
        module_a.dostuff()

        subcommand = getattr(args, "subcommand", None)

        if subcommand:
            subcommand_args = getattr(args, "subcommand_args", None)  # noqa: F841
            level2.dostuff()

            subsubcommand = getattr(args, "subsubcommand", None)

            if subsubcommand:
                subsubcommand_args = getattr(  # noqa: F841
                    args, "subsubcommand_args", None
                )
                level3.dostuff()

                subsubsubcommand = getattr(args, "subsubsubcommand", None)

                if subsubsubcommand:
                    subsubsubcommand_args = getattr(  # noqa: F841
                        args, "subsubsubcommand_args", None
                    )
                    level4.dostuff()

                    subsubsubsubcommand = getattr(args, "subsubsubsubcommand", None)

                    if subsubsubsubcommand:
                        subsubsubsubcommand_args = getattr(  # noqa: F841
                            args, "subsubsubsubcommand_args", None
                        )
                        module_b.dostuff()

    _logger.info("Script ends here")


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
