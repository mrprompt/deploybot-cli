# -*- coding: utf-8 -*-
from unittest import TestCase
from deploybot.server import Server
import mock

Client = mock.Mock()


class TestServer(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        self.server = Server(Client())

    # test servers list
    def test_list(self):
        self.assertNotEquals("", self.server.list())

    # test server get
    def test_get(self):
        self.assertNotEquals("", self.server.get(125815))
