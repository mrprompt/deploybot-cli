# -*- coding: utf-8 -*-
from unittest import TestCase
from deploybot.deploy import Deploy


class TestDeploy(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        self.deploy = Deploy()

    # test deployments list
    def test_list_must_be_return_json(self):
        self.assertNotEquals('', self.deploy.list('77289', '92033'))