# -*- coding: utf-8 -*-
from deploybot.scripts import cli
from unittest import TestCase
from click.testing import CliRunner


class TestCli(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        self.runner = CliRunner()

    def test_cli(self):
        result = self.runner.invoke(cli.main(), ['help'])

        assert result.exit_code == -1
