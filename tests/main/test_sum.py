# https://click.palletsprojects.com/en/8.0.x/testing/


from click.testing import CliRunner
from src.main import cli


def test_sum():
    runner = CliRunner()
    result = runner.invoke(cli, ["--debug", "sum", "2", "3"])
    assert result.exit_code == 0
    assert str(5) in result.output
    assert "debug" in result.output.casefold()

    result = runner.invoke(cli, ["sum", "--", "2", "3", "-1"])
    assert result.exit_code == 0
    assert str(4) in result.output
