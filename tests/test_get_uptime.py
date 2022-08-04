#!/usr/bin/env python

import unittest

import check_uptime


class GetUptimeTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_uptime(self):
        uptime_sec = check_uptime.get_uptime(uptime_file="tests/examples/proc_uptime")
        self.assertEqual(uptime_sec, 10043.27)
