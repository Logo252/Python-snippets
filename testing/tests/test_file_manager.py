# -*- coding: utf-8 -*-

import shutil
import tempfile
import unittest


class TestMoveFile(unittest.TestCase):
    """Test for the 'move_file' function."""

    @classmethod
    def setUpClass(cls):
        cls.test_directory = tempfile.mkdtemp()
        cls.invalid_directory = "Test"

    def test_with_correct_values(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_directory)


class TestCopyFile(unittest.TestCase):
    """Test for the 'copy_file' function."""

    @classmethod
    def setUpClass(cls):
        cls.test_directory = tempfile.mkdtemp()
        cls.invalid_directory = "Test"

    def test_with_correct_values(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_with_correct_values(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_directory)

# if __name__ == '__main__':
#     unittest.main()

# python -m unittest -v test_file_manager
