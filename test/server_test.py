from unittest import TestCase
from click.testing import CliRunner
from cli.server import server


class TestServer(TestCase):
    def setUp(self):
        TestCase.setUp(self)

    def test_server_list(self):
        runner = CliRunner()
        result = runner.invoke(server, ['list'])

        assert result.exit_code == 0
        assert result.output != ""

    def test_server_get(self):
        runner = CliRunner()
        result = runner.invoke(server, ['get', '125815'])

        assert result.exit_code == 0
        assert result.output != ""
