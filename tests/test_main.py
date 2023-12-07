import re

import pytest

from busyauthor.main import main

__author__ = "Taylor Monacelli"
__copyright__ = "Taylor Monacelli"
__license__ = "MPL-2.0"


def test_main_with_invalid_argument(capsys):
    """Test CLI with an invalid argument"""
    with pytest.raises(SystemExit) as e:
        main(["invalid_argument"])

    assert e.value.code == 2

    captured = capsys.readouterr()
    assert "invalid choice:" in captured.err.lower()


def test_main_with_verbose_flag(caplog):
    """Test CLI with verbose flag"""
    main(["--verbose"])

    assert any(
        "Starting crazy calculations..." not in record.message
        for record in caplog.records
    )
    assert any("Script ends here" in record.message for record in caplog.records)


def test_main_with_version_flag(capfd):
    """Test CLI with version flag"""
    with pytest.raises(SystemExit) as e:
        main(["--version"])
    assert e.value.code == 0
    captured = capfd.readouterr()
    assert "busyauthor 0.0" in captured.out


def test_main_with_very_verbose_flag(caplog):
    """Test CLI with verbose flag"""
    main(["--very-verbose"])

    assert any(
        "Starting crazy calculations..." in record.message for record in caplog.records
    )
    assert any("Script ends here" in record.message for record in caplog.records)


def test_main_with_no_argument(capfd):
    """Test CLI with missing argument"""
    main([])
    captured = capfd.readouterr()
    assert captured.err.strip() == ""
    assert captured.out.strip() == ""


def test_main_with_zero_argument(capfd):
    """Test CLI with zero as an argument"""
    with pytest.raises(SystemExit) as e:
        main(["0"])

    captured = capfd.readouterr()
    assert e.value.code == 2
    assert "invalid choice: '0'" in captured.err.lower()


def test_main_with_multiple_invalid_values(capfd):
    """Test CLI with multiple values as arguments"""
    with pytest.raises(SystemExit) as e:
        main(["3", "5", "8"])

    assert e.value.code == 2
    captured = capfd.readouterr()
    assert "invalid choice: '3'" in captured.err.lower()


def test_main_with_help_param(capfd):
    """Test CLI with help argument"""
    with pytest.raises(SystemExit):
        main(["--help"])
    captured = capfd.readouterr()
    assert captured.err == ""
    assert "show this help message" in captured.out.lower()
    assert "command,cmd" in captured.out.lower()
    assert "command2,cmd2" in captured.out.lower()


def test_main_with_command_subcommand(capfd):
    """Test CLI with help argument"""
    main(["command"])
    captured = capfd.readouterr()
    assert captured.err.strip() == ""
    assert captured.out.strip() == "doing work in command"


def test_main_with_subcommand_out_of_order(capfd):
    """Test CLI with subcommand as first argument"""
    with pytest.raises(SystemExit) as e:
        main(["subcommand"])
    assert e.value.code == 2


def test_main_with_command_and_subcommit_in_proper_order(capfd):
    """Test CLI with subcommand as first argument"""
    main(["command", "subcommand"])
    captured = capfd.readouterr()
    assert captured.err.strip() == ""

    captured_out = captured.out.strip()
    pattern = r"doing work in subcommand$"

    assert re.search(
        pattern, captured_out
    ), f"Pattern '{pattern}' not found in the captured output:\n{captured_out}"


def test_main_commmand(capfd):
    """Test CLI with subcommand as first argument"""
    with pytest.raises(SystemExit) as e:
        main(["command2", "subcommand"])
    assert e.value.code == 2
    captured = capfd.readouterr()
    assert "error: unrecognized arguments: subcommand" in captured.err
    assert captured.out.strip() == ""


def test_main_with_command2_no_subcommand(capfd):
    """Test CLI with subcommand as first argument"""
    main(["command"])
    captured = capfd.readouterr()
    assert captured.out.strip() == "doing work in command"


def test_main_with_command2_subcommand(capfd):
    """Test CLI with help argument"""
    main(["command2"])
    captured = capfd.readouterr()
    assert captured.err.strip() == ""
    assert captured.out.strip() == "doing work in command2"


def test_main_with_command2_with_arg(capfd):
    """Test CLI with help argument"""
    main(["cmd2", "--command2", "test"])
    captured = capfd.readouterr()
    assert captured.err.strip() == ""
    assert captured.out.strip() == "doing work in command2"


def test_main_with_command3_alias_subcommand(capfd):
    """Test CLI with help argument"""
    main(["command3", "-v", "--command3-args", "test"])
    captured = capfd.readouterr()
    assert "INFO:busyauthor.main:Script ends here" in captured.err
    assert "command3_args='test'" in captured.out.strip()


def test_main_with_subsubcommand(capfd):
    """Test CLI with help argument"""
    main(["cmd", "subcmd", "subsubcmd"])
    captured = capfd.readouterr()
    assert captured.err.strip() == ""
    assert "doing work in command" in captured.out
    assert "doing work in subcommand" in captured.out
    assert "doing work in subsubcommand" in captured.out

    captured_out = captured.out.strip()
    expected_pattern = "doing work in subsubcommand"
    last_line = captured_out.splitlines()[-1]
    assert (
        last_line == expected_pattern
    ), f"Last line does not match the expected pattern: {last_line}"


def test_main_with_subsubsubcommand(capfd):
    """Test CLI with help argument"""
    main(["cmd", "subcmd", "subsubcmd", "subsubsubcmd"])
    captured = capfd.readouterr()
    assert captured.err.strip() == ""
    assert "doing work in command" in captured.out
    assert "doing work in subcommand" in captured.out
    assert "doing work in subsubcommand" in captured.out
    assert "doing work in subsubsubcommand" in captured.out

    captured_out = captured.out.strip()
    expected_pattern = "doing work in subsubsubcommand"
    last_line = captured_out.splitlines()[-1]
    assert (
        last_line == expected_pattern
    ), f"Last line does not match the expected pattern: {last_line}"


def test_main_with_subsubsubsubcommand(capfd):
    """Test CLI with help argument"""
    main(["cmd", "subcmd", "subsubcmd", "subsubsubcmd", "subsubsubsubcmd"])
    captured = capfd.readouterr()
    assert captured.err.strip() == ""
    assert "doing work in command" in captured.out
    assert "doing work in subcommand" in captured.out
    assert "doing work in subsubcommand" in captured.out
    assert "doing work in subsubsubcommand" in captured.out
    assert "doing work in subsubsubsubcommand" in captured.out

    captured_out = captured.out.strip()
    expected_pattern = "doing work in subsubsubsubcommand"
    last_line = captured_out.splitlines()[-1]
    assert (
        last_line == expected_pattern
    ), f"Last line does not match the expected pattern: {last_line}"


def test_main_with_subsubsubcommand_with_args(capfd):
    """Test CLI with help argument"""
    main(["cmd", "subcmd", "subsubcmd", "subsubsubcmd", "--subsubsubcommand-args", "2"])
    captured = capfd.readouterr()
    assert "args.subsubsubcommand_args='2'" in captured.out.strip()


def test_main_with_subsubsubcommand_wit_very_verbose(capfd):
    """Test CLI with help argument"""
    main(
        [
            "cmd",
            "subcmd",
            "subsubcmd",
            "subsubsubcmd",
            "--subsubsubcommand-args",
            "2",
            "--very-verbose",
        ]
    )
    captured = capfd.readouterr()
    assert "args.subsubsubcommand_args='2'" in captured.out.strip()
    assert "Starting crazy calculations..." in captured.err.strip()
