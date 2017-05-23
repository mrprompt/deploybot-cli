# -*- coding: utf-8 -*-
from unittest import TestCase
from deploybot.user import User
import mock

Client = mock.Mock()


class TestUser(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        self.user = User(Client())

    # test users list
    def test_list(self):
        self.assertNotEquals("", self.user.list())

    # test users get
    def test_get(self):
        self.assertNotEquals("", self.user.get('46964'))
