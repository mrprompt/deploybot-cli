# -*- coding: utf-8 -*-
from unittest import TestCase
from deploybot.environment import Environment


class TestEnvironment(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        self.environment = Environment()

    # test environments list
    def test_list_without_parameter(self):
        self.assertNotEquals("", self.environment.list())

    # test environments list
    def test_list_with_repository_parameter(self):
        self.assertNotEquals("", self.environment.list(1900))

    # test environment get
    def test_get(self):
        self.assertNotEquals("", self.environment.get(106090))