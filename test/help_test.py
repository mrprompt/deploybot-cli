# -*- coding: utf-8 -*-
from unittest import TestCase
from cli.help import Help


class TestHelper(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        self.help = Help()

    # test repositories list
    def test_list_must_be_return_json(self):
        self.assertNotEquals("", self.help.list())