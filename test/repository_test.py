# -*- coding: utf-8 -*-
from unittest import TestCase
from deploybot.repository import Repository
import mock

Client = mock.Mock()


class TestRepository(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        self.repository = Repository(Client())

    # test repositories list
    def test_list(self):
        self.assertNotEquals("", self.repository.list())

    # test repositories get
    def test_get(self):
        self.assertNotEquals("", self.repository.get('109294'))