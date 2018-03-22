# -*- coding: utf-8 -*-

import os
import shutil
import unittest

from testing import file_manager as fm


class TestMoveFile(unittest.TestCase):
    """Test for the 'move_file' function."""

    @classmethod
    def setUpClass(cls):
        cls.cwd = os.getcwd()

        cls.test_directory = 'output_folder'
        cls.test_file_name = 'input_file.txt'
        cls.test_file = os.path.join(cls.cwd, cls.test_file_name)
        with open(cls.test_file, 'w') as _file:
            _file.write("Content")

        cls.invalid_directory = 55
        cls.invalid_file = 'Test'

    def test_with_correct_values(self):
        """Should return new path to the moved file without any errors."""
        self.assertEqual(fm.move_file(self.test_file, self.test_directory),
                         "{}".format(os.path.join(self.cwd, self.test_directory, self.test_file_name)))

    def test_with_invalid_input_file(self):
        """Should raise an IOError exception."""
        with self.assertRaises(IOError):
            fm.move_file(self.invalid_file, self.test_directory)

    def test_with_invalid_output_folder(self):
        """Should raise an TypeError exception."""
        with self.assertRaises(TypeError):
            fm.move_file(self.test_file, self.invalid_directory)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_directory, ignore_errors=True)
        try:
            os.remove(cls.test_file)
        except OSError:
            pass


class TestCopyFile(unittest.TestCase):
    """Test for the 'copy_file' function."""

    @classmethod
    def setUpClass(cls):
        cls.test_directory = 'output_folder'
        cls.test_file_name = os.path.basename(__file__)
        cls.test_file = __file__

        cls.invalid_directory = 55
        cls.invalid_file = 'Test'

    def test_with_correct_values(self):
        """Should return new path to the copied file without any errors."""
        self.assertEqual(fm.copy_file(self.test_file, self.test_directory),
                         "{}".format(os.path.join(os.getcwd(), self.test_directory, self.test_file_name)))

    def test_with_invalid_input_file(self):
        """Should raise an IOError exception."""
        with self.assertRaises(IOError):
            fm.copy_file(self.invalid_file, self.test_directory)

    def test_with_invalid_output_folder(self):
        """Should raise an TypeError exception."""
        with self.assertRaises(TypeError):
            fm.copy_file(self.test_file, self.invalid_directory)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_directory, ignore_errors=True)

# if __name__ == '__main__':
#     unittest.main()

# python -m unittest -v test_file_manager

# python module.py -v
# python module.py
