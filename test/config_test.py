from unittest import TestCase
from cli.config import Config

import os

class TestConfig(TestCase):
    def setUp(self):
        TestCase.setUp(self)

    def test_config_contains_default_attributes(self):
        config = Config()

        self.assertEquals(config.width, 32)
        self.assertEquals(config.style, 'fancy_grid')
        self.assertIsInstance(config.client, object)
        self.assertEquals(config.account, os.environ.get('DEPLOYBOT_ACCOUNT'))
        self.assertEquals(config.token, os.environ.get('DEPLOYBOT_TOKEN'))
