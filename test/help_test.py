# -*- coding: utf-8 -*-
from unittest import TestCase
from deploybot.help import Help


class TestHelp(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        self.help = Help()

    # test repositories list
    def test_list_must_be_return_json(self):
        self.assertNotEquals("", self.help.list)