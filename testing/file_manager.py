# -*- coding: utf-8 -*-


import os
import shutil


def move_file(input_file, output_folder):
    """Moves given file to the specified folder. Returns a new path of the file."""
    output_file = copy_file(input_file, output_folder)
    if output_file:
        os.remove(input_file)
    return output_file


def copy_file(input_file, output_folder):
    """Copies given file to the specified folder. Returns a new path of the file."""
    _create_directory(output_folder)

    output_file = os.path.join(output_folder, os.path.basename(input_file))
    shutil.copy2(input_file, output_file)

    return os.path.abspath(output_file)


def _create_directory(path_to_dir):
    """Creates a directory if it is missing."""
    if not os.path.exists(path_to_dir):
        os.makedirs(path_to_dir)


if __name__ == '__main__':
    cwd = os.getcwd()

    test_file = os.path.join(cwd, 'test.txt')
    if not os.path.isfile(test_file):
        open(test_file, 'w').close()
    print(move_file(test_file, 'examples'))

    python_file = os.path.join(cwd, 'boxer.py')
    print(copy_file(python_file, 'examples'))
