from unittest import TestCase
from unittest_data_provider import data_provider
from cli import body, response
import mock
import sys
import json

mock_stdout = mock.Mock()
sys.stdout = mock_stdout


class TestCli(TestCase):
    def setUp(self):
        TestCase.setUp(self)

    commands = lambda: (
        (
            ("help", "list", {'command': True, 'description': True, 'params': True}),
            ("repository", "list", {'id': True, 'name': True, 'title': True}),
            ("repository", "get", [True, True, True, True, True, True, True, True]),
            ("user", "list",
             {'id': True, 'first_name': 'foo', 'last_name': 'bar', 'email': 'foo@bar.bar', 'is_admin': 0}),
            ("user", "get", ["nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono"]),
            ("environment", "list",
             {'id': True, 'repository_id': '0', 'name': 'bar', 'branch_name': 'foo', 'is_automatic': 0,
              'current_version': 0}),
            ("environment", "get",
             ["nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono"]),
            ("deploy", "list",
             {'id': True, 'repository_id': '0', 'environment_id': '0', 'state': 'foo', 'deployed_version': 0}),
            ("deploy", "get",
             ["nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono",
              "nono"]),
            ("deploy", "trigger",
             ["nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono",
              "nono"]),
            ("server", "list", {'id': True, 'environment_id': '0', 'name': 'foo', 'protocol': "foo"}),
            ("server", "get", ["nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono", "nono"]),
        )
    )

    @data_provider(commands)
    def test_body_return_class_with_valid_command(self, command="", parameter="", result={}):
        self.assertIsInstance(body(command, parameter, result), list)

    def test_response_with_list_param(self):
        json_content = {
            "meta": {
                "next": 1,
                "next_uri": 1,
                "total": 1
            },
            "entries": [
                {
                    "id": 1,
                    "first_name": "Foo",
                    "last_name": "Bar",
                    "timezone": "Brasilia",
                    "email": "foo@bar.bar",
                    "created_at": "2015/02/19 21:53:42 +0000",
                    "updated_at": "2015/03/01 20:02:49 +0000",
                    "is_admin": True
                }
            ]
        }

        json_result = json.dumps(json_content)

        self.assertNotEquals("", response("user", "list", json_result))

    def test_response_with_valid_get_parameter_return_valid(self):
        json_content = {
            "id": 43,
            "name": "example-repo",
            "title": "Example repository",
            "color_label": "label-green-blue",
            "type": "GitRepository",
            "url": "https://github.com/wildbit/pexample-repo.git",
            "refresh_webhook_url": "https://support.deploybot.com/webhook/qwertysecrethash",
            "created_at": "2015/02/19 21:53:42 +0000",
            "updated_at": "2015/03/01 20:02:49 +0000"
        }

        json_result = json.dumps(json_content)

        self.assertNotEquals("", response("user", "get", json_result))
