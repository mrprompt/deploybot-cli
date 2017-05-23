# -*- coding: utf-8 -*-
from deploybot.scripts import cli
from unittest import TestCase


class TestCli(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

    def test_main(self):
        result = cli.main()

        self.assertEquals(None, result)

    def test_run(self):
        self.assertRaises(TypeError, cli.run())

    def test_headers(self):
        self.assertRaises(TypeError, cli.headers())

    def test_body(self):
        self.assertRaises(TypeError, cli.body())
