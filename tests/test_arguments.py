#!/usr/bin/env python

import unittest

import check_uptime


class ArgumentsTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_parse_arguments(self):
        args = check_uptime.parse_arguments(["--min-days", "1", "--max-days", "2"])
        self.assertEqual(args.min_days, 1)
        self.assertEqual(args.max_days, 2)
