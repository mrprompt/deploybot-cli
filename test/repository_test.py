# -*- coding: utf-8 -*-
from unittest import TestCase
from deploybot.repository import Repository


class TestRepository(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        self.repository = Repository()

    # test repositories list
    def test_list(self):
        self.assertNotEquals("", self.repository.list())

    # test repositories get
    def test_get(self):
        self.assertNotEquals("", self.repository.get('109294'))