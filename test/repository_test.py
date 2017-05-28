from unittest import TestCase
from click.testing import CliRunner
from cli.repository import repository


class TestRepository(TestCase):
    def setUp(self):
        TestCase.setUp(self)

    def test_repository_list(self):
        runner = CliRunner()
        result = runner.invoke(repository, ['list'])

        assert result.exit_code == 0
        assert result.output != ""

    def test_repository_get(self):
        runner = CliRunner()
        result = runner.invoke(repository, ['get', '109294'])

        assert result.exit_code == 0
        assert result.output != ""
