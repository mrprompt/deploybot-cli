# -*- coding: utf-8 -*-
from unittest import TestCase
from deploybot.repository import Repository


class TestRepository(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        self.repository = Repository()

    # test repositories list
    def test_list_must_be_return_json(self):
        self.assertNotEquals("", self.repository.list())