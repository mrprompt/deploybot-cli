# -*- coding: utf-8 -*-
from unittest import TestCase
from deploybot.client import Client
import python_http_client


class TestClient(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        self.client = Client()

    # Tests de default url raises an error without parameters
    def test_get_url_without_parameter(self):
        self.assertRaises(TypeError, self.client.get_url())

    # Tests de default url return a full url
    def test_get_url_with_account_parameter(self):
        result_expected = "https://test.deploybot.com/api/v1/"

        self.assertEqual(result_expected, self.client.get_url("test"))

    # Tests de default url return a full url
    def test_get_url_with_endpoint_parameter(self):
        result_expected = "https://test.deploybot.com/api/v1/deploy"

        self.assertEqual(result_expected, self.client.get_url("test", "deploy"))

    # Test get_client
    def test_get_client_must_be_return_instance_of_client(self):
        self.assertIsInstance(self.client.get_client(), python_http_client.Client)
