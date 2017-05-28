from unittest import TestCase
from click.testing import CliRunner
from cli.deploy import deploy


class TestDeploy(TestCase):
    def setUp(self):
        TestCase.setUp(self)

    def test_deploy_list(self):
        runner = CliRunner()
        result = runner.invoke(deploy, ['list', '77289', '92033'])

        assert result.exit_code == 0
        assert result.output != ""

    def test_deploy_get(self):
        runner = CliRunner()
        result = runner.invoke(deploy, ['get', '7929622'])

        assert result.exit_code == 0
        assert result.output != ""

    def test_deploy_trigger(self):
        self.skipTest('dont do this')
        runner = CliRunner()
        result = runner.invoke(deploy, ['trigger', '91944'])

        assert result.exit_code == 0
        assert result.output != ""
