#!/usr/bin/env python

import sys
import unittest
from mock import patch

import check_uptime


class MainTestCase(unittest.TestCase):
    def setUp(self):
        pass

    @patch("check_uptime.get_uptime")
    def test_main(self, mock_get_uptime):
        #
        # Test with no issues
        #
        with patch.object(sys, "argv", ["check_uptime.py"]):
            mock_get_uptime.return_value = 1

            self.assertEqual(check_uptime.main(), 0)

        #
        # Test with min-days failure
        #
        with patch.object(sys, "argv", ["check_uptime.py", "--min-days", "2"]):
            mock_get_uptime.return_value = 100.2

            self.assertEqual(check_uptime.main(), 1)

        #
        # Test with max-days failure
        #
        with patch.object(sys, "argv", ["check_uptime.py", "--max-days", "2"]):
            mock_get_uptime.return_value = 172801.2

            self.assertEqual(check_uptime.main(), 1)
