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

import mock
import sys

mock_stdout = mock.Mock()
sys.stdout = mock_stdout


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
    def test_run_return_class_with_valid_command(self, command="", instance=object):
        result = cli.run(command)

        self.assertIsInstance(result, instance)

    def test_headers_raises_index_error_with_unknown_command(self):
        self.assertRaises(IndexError, cli.headers, ["default"])

    def test_headers_raises_type_error_without_command(self):
        self.assertRaises(TypeError, cli.headers)

    commands = lambda: (
        (
            ("help", 3),
            ("repository", 3),
            ("user", 4),
            ("environment", 6),
            ("deploy", 5),
            ("server", 4),
        )
    )

    @data_provider(commands)
    def test_headers_return_return_with_valid_command(self, command="", size=0):
        result = cli.headers(command)

        self.assertEquals(len(result), size)

    def test_body_raises_index_error_with_unknown_command(self):
        self.assertRaises(IndexError, cli.body, *["default", "default", {}])

    def test_body_raises_type_error_parameters(self):
        self.assertRaises(TypeError, cli.body)

    commands = lambda: (
        (
            ("help", "list", {'command': True, 'description': True, 'params': True}),
            ("repository", "list", {'id': True, 'name': True, 'title': True}),
            ("repository", "get", [True, True, True, True, True, True, True, True]),
            ("user", "list", {'id': True, 'first_name': 'foo', 'last_name': 'bar', 'email': 'foo@bar.bar', 'is_admin': 0}),
            ("user", "get", ["nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono"]),
            ("environment", "list", {'id': True, 'repository_id': '0', 'name': 'bar', 'branch_name': 'foo', 'is_automatic': 0, 'current_version': 0}),
            ("environment", "get", ["nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono"]),
            ("deploy", "list", {'id': True, 'repository_id': '0', 'environment_id': '0', 'state': 'foo', 'deployed_version': 0}),
            ("deploy", "get", ["nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono"]),
            ("deploy", "trigger", ["nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono"]),
            ("server", "list", {'id': True, 'environment_id': '0', 'name': 'foo', 'protocol': "foo"}),
            ("server", "get", ["nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono"]),
        )
    )

    @data_provider(commands)
    def test_body_return_class_with_valid_command(self, command="", parameter="", result={}):
        self.assertIsInstance(cli.body(command, parameter, result), list)

    def test_main(self):
        result = cli.main(sys.stdout)

        self.assertNotEquals("", result)
