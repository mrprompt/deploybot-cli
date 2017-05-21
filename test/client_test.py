# -*- coding: utf-8 -*-

from unittest import TestCase
from deploybot.client import Client

class TestClient(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        self.client = Client()

    # Tests de default url raises an error without parameters
    def test_getUrlWithoutParameters(self):
        self.assertRaises(TypeError, self.client.getUrl)

    # Tests de default url return a full url
    def test_getUrlWithParameter(self):
        result_expected = "https://test.deploybot.com/api/v1"

        self.assertEqual(result_expected, self.client.getUrl("test"))
