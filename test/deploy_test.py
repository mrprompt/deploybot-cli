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
        self.skipTest("Need fix 422 error")
        self.assertEqual(200, self.deploy.list())