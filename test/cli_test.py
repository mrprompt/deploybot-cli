import os

import cli
from unittest import TestCase
from click.testing import CliRunner


class TestCli(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        self.runner = CliRunner()

    def test_cli_without_parameter_show_help(self):
        result = self.runner.invoke(cli)

        assert result.exit_code == -1