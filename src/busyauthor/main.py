import logging
import sys

from busyauthor import main_args

__author__ = "Taylor Monacelli"
__copyright__ = "Taylor Monacelli"
__license__ = "MPL-2.0"

_logger = logging.getLogger(__name__)


def setup_logging(loglevel):
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def print_command_hierarchy(args):
    db_file = args.db
    command = getattr(args, "command", None)
    command_args = getattr(args, "command_args", None)
    subcommand = getattr(args, "subcommand", None)
    subcommand_args = getattr(args, "subcommand_args", None)
    subsubcommand = getattr(args, "subsubcommand", None)
    subsubcommand_args = getattr(args, "subsubcommand_args", None)
    subsubsubcommand = getattr(args, "subsubsubcommand", None)
    subsubsubcommand_args = getattr(args, "subsubsubcommand_args", None)

    print(f"Database File: {db_file}")

    if command:
        print(f"Command: {command}")
        print(f"Command Args: {command_args}")

        if subcommand:
            print(f"Subcommand: {subcommand}")
            print(f"Subcommand Args: {subcommand_args}")

            if subsubcommand:
                print(f"Subsubcommand: {subsubcommand}")
                print(f"Subsubcommand Args: {subsubcommand_args}")

                if subsubsubcommand:
                    print(f"Subsubsubcommand: {subsubsubcommand}")
                    print(f"Subsubsubcommand Args: {subsubsubcommand_args}")


def main(args):
    args = main_args.parser.parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    print_command_hierarchy(args)
    _logger.info("Script ends here")


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
