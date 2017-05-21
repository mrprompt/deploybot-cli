# -*- coding: utf-8 -*-
from unittest import TestCase
from deploybot.server import Server


class TestServer(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        self.server = Server()

    # test servers list
    def test_list_must_be_return_json(self):
        self.assertNotEquals("", self.server.list())