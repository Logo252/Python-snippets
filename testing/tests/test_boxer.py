# -*- coding: utf-8 -*-

import unittest
from unittest import mock

import requests

from testing.boxer import Boxer


class TestBoxer(unittest.TestCase):
    """Test for the Boxer class."""

    @classmethod
    def setUpClass(cls):
        print("setupClass")
        cls.boxing_url = "https://boxingschedule.boxingsociety.com"

    def setUp(self):
        print("setUp")
        self.boxer_1 = Boxer(first_name='Corey', last_name='Schafer')
        self.boxer_2 = Boxer(first_name='Sue', last_name='Smith')

    def tearDown(self):
        print("tearDown")

    def test_full_name(self):
        """Shouldn't raise any exception!"""
        print('test_full_name')

        self.assertEqual(self.boxer_1.full_name, 'Corey Schafer')
        self.assertEqual(self.boxer_2.full_name, 'Sue Smith')

        self.boxer_1.first_name = 'John'
        self.boxer_2.first_name = 'Jane'

        self.assertEqual(self.boxer_1.full_name, 'John Schafer')
        self.assertEqual(self.boxer_2.full_name, 'Jane Smith')

    def test_get_next_opponent(self):
        """Shouldn't raise any exception!"""
        print('test_get_next_opponent')

        # Using context manager instead of decorator
        with mock.patch("requests.get") as mock_requests_get:
            # Test responses and used arguments
            mock_requests_get.return_value = None

            next_opponent = self.boxer_2.get_next_opponent()
            mock_requests_get.assert_called_with('{}/SueSmith/next-opponent'.format(self.boxing_url))
            self.assertEqual(next_opponent, Boxer.BAD_REQUEST_MESSAGE_NEXT_OPPONENT)

            # Test multiple side effects
            mock_requests_get.side_effect = ["First opponent", UnboundLocalError, "Second opponent"]
            self.assertEqual(self.boxer_2.get_next_opponent(), "First opponent")

            with self.assertRaises(UnboundLocalError):
                self.boxer_2.get_next_opponent()

            self.assertEqual(self.boxer_2.get_next_opponent(), "Second opponent")

            # Raises an exception calling method again
            # self.boxer_2.get_next_opponent()

            # Test calls
            mock_requests_get.assert_called()
            # mock_requests_get.assert_called_once()
            # mock_requests_get.assert_not_called()

    @unittest.mock.patch("requests.get")
    def test_get_upcoming_fights(self, mock_requests_get):
        """Shouldn't raise any exception!"""
        print('test_get_upcoming_fights')

        # Test responses and used arguments
        mock_requests_get.return_value.ok = True
        mock_requests_get.return_value.text = 'Success'

        fights = self.boxer_1.get_upcoming_fights(month='May')
        mock_requests_get.assert_called_with('{}/fights/May/CoreySchafer'.format(self.boxing_url))
        self.assertEqual(fights, 'Success')

        mock_requests_get.return_value.ok = False

        fights = self.boxer_2.get_upcoming_fights(month='June')
        mock_requests_get.assert_called_with('{}/fights/June/SueSmith'.format(self.boxing_url))
        self.assertEqual(fights, Boxer.BAD_REQUEST_MESSAGE_UPCOMING_FIGHTS)

        # Test exceptions
        mock_requests_get.side_effect = ValueError
        with self.assertRaises(ValueError):
            self.boxer_1.get_statistics()
            self.boxer_2.get_statistics()

    def _mocked_requests_get(*args):
        """This method will be used by the mock to replace requests.get method."""

        class MockedResponse:
            """Contains Mocked response attributes."""

            def __init__(self, ok, text=None):
                self.ok = ok
                self.text = text

        return MockedResponse(True, 'Success') if 'CoreySchafer' in args[0] else MockedResponse(False)

    @mock.patch("requests.post", return_value='Post')
    @mock.patch("requests.get", side_effect=_mocked_requests_get)
    def test_get_statistics(self, mock_requests_get, mock_requests_post):
        """Shouldn't raise any exception!"""
        print('test_get_statistics')

        # Test requests.post response
        self.assertEqual(requests.post("Test URL"), "Post")

        # Test responses and used arguments
        statistics = self.boxer_1.get_statistics()
        mock_requests_get.assert_called_with('{}/statistics/CoreySchafer'.format(self.boxing_url))
        self.assertEqual(statistics, 'Success')

        statistics = self.boxer_2.get_statistics()
        mock_requests_get.assert_called_with('{}/statistics/SueSmith'.format(self.boxing_url))
        self.assertEqual(statistics, Boxer.BAD_REQUEST_MESSAGE_STATISTICS)

        # Test exceptions
        mock_requests_get.side_effect = TypeError
        with self.assertRaises(TypeError):
            self.boxer_1.get_statistics()

        mock_requests_get.side_effect = ValueError
        with self.assertRaises(ValueError):
            self.boxer_2.get_statistics()

    @classmethod
    def tearDownClass(cls):
        print("teardownClass")


if __name__ == '__main__':
    unittest.main()

# python -m unittest -v test_boxer

# python module.py -v
# python module.py
