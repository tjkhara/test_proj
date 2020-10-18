import unittest
from testing import ugen

class TestUgen(unittest.TestCase):

    def test_read_input_does_not_crash_diff_dir(self):
        """
        read_input() does not crash when input file is in diff dir path "../input/file1"
        """
        ugen.read_input("../input/file1")

    def test_read_input_does_not_crash_same_dir(self):
        """
        read_input() does not crash when input file is in same dir path "./file1"
        """
        ugen.read_input("./file1")

    def test_read_input_does_not_crash_same_dir_filename(self):
        """
        read_input() does not crash when input file is in same dir path with just filename "file1"
        """
        ugen.read_input("file1")