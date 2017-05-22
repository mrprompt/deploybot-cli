# -*- coding: utf-8 -*-
from unittest import TestCase
from deploybot.deploy import Deploy


class TestDeploy(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        self.deploy = Deploy()

    # test deployments list
    def test_list(self):
        self.assertNotEquals('', self.deploy.list('77289', '92033'))

    # test deployment get
    def test_get(self):
        self.assertNotEquals('', self.deploy.get('7929622'))

    # test deployment trigger
    def test_trigger(self):
        self.assertNotEquals('', self.deploy.trigger('106088'))
