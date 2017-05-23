# -*- coding: utf-8 -*-
from deploybot.scripts import cli
from unittest import TestCase
from unittest_data_provider import data_provider
from deploybot.deploy import Deploy
from deploybot.user import User
from deploybot.repository import Repository
from deploybot.environment import Environment
from deploybot.server import Server
from deploybot.help import Help

class TestCli(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

    def test_run_raises_index_error_with_unknown_command(self):
        self.assertRaises(IndexError, cli.run, ["default"])

    def test_run_raises_type_error_without_command(self):
        self.assertRaises(TypeError, cli.run)

    def test_run_return_class_with_valid_command(self):
        self.assertIsInstance(cli.run("help"), object)

    commands = lambda: (
        (
            ("help", Help),
            ("repository", Repository),
            ("user", User),
            ("environment", Environment),
            ("deploy", Deploy),
            ("server", Server),
        )
    )

    @data_provider(commands)
    def test_run_return_class_with_all_commands(self, command="", instance=object):
        result = cli.run(command)

        self.assertIsInstance(result, instance)

    def test_headers_raises_index_error_with_unknown_command(self):
        self.assertRaises(IndexError, cli.headers, ["default"])

    def test_headers_raises_type_error_without_command(self):
        self.assertRaises(TypeError, cli.headers)

    def test_headers_return_class_with_valid_command(self):
        self.assertIsInstance(cli.headers("help"), object)

    def test_body_raises_index_error_with_unknown_command(self):
        self.assertRaises(IndexError, cli.body, *["default", "default", {}])

    def test_body_raises_type_error_parameters(self):
        self.assertRaises(TypeError, cli.body)

    def test_body_return_class_with_valid_command(self):
        item = {'command': True, 'description': True, 'params': True};

        self.assertIsInstance(cli.body("help", "list", item), object)

    def test_main(self):
        self.skipTest("Not implemented")
        self.assertEquals(None,  cli.main())
