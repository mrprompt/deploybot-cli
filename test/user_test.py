from unittest import TestCase
from click.testing import CliRunner
from cli.user import user


class TestUser(TestCase):
    def setUp(self):
        TestCase.setUp(self)

    def test_user_list(self):
        runner = CliRunner()
        result = runner.invoke(user, ['list'])

        assert result.exit_code == 0
        assert result.output != ""

    def test_user_get(self):
        runner = CliRunner()
        result = runner.invoke(user, ['get', '46964'])

        assert result.exit_code == 0
        assert result.output != ""
