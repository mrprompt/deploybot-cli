from unittest import TestCase
from click.testing import CliRunner
from cli.environment import environment


class TestEnvironment(TestCase):
    def setUp(self):
        TestCase.setUp(self)

    def test_environment_list_without_repository(self):
        runner = CliRunner()
        result = runner.invoke(environment, ['list'])

        assert result.exit_code == 2
        assert result.output != ""

    def test_environment_list_with_repository(self):
        runner = CliRunner()
        result = runner.invoke(environment, ['list', '106090'])

        assert result.exit_code == 0
        assert result.output != ""

    def test_environment_get(self):
        runner = CliRunner()
        result = runner.invoke(environment, ['get', '106090'])

        assert result.exit_code == 0
        assert result.output != ""
