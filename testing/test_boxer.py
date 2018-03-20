# -*- coding: utf-8 -*-

import unittest

import mock

from boxer import Boxer


class TestBoxer(unittest.TestCase):
    """Test for the Boxer class."""

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.boxer_1 = Boxer('Corey', 'Schafer', 50000)
        self.boxer_2 = Boxer('Sue', 'Smith', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.boxer_1.full_name, 'Corey Schafer')
        self.assertEqual(self.boxer_2.full_name, 'Sue Smith')

        self.boxer_1.first_name = 'John'
        self.boxer_2.first_name = 'Jane'

        self.assertEqual(self.boxer_1.full_name, 'John Schafer')
        self.assertEqual(self.boxer_2.full_name, 'Jane Smith')

    @mock.patch("boxer.requests.get")
    def test_get_upcoming_fights(self, mock_requests_get):
        mock_requests_get.return_value.ok = True
        mock_requests_get.return_value.text = 'Success'

        fights = self.boxer_1.get_upcoming_fights('May')
        mock_requests_get.assert_called_with('https://boxingschedule.boxingsociety.com/fights/May/CoreySchafer')
        self.assertEqual(fights, 'Success')

        mock_requests_get.return_value.ok = False

        fights = self.boxer_2.get_upcoming_fights('June')
        mock_requests_get.assert_called_with('https://boxingschedule.boxingsociety.com/fights/June/SueSmith')
        self.assertEqual(fights, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
