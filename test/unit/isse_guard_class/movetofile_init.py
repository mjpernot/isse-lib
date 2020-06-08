#!/usr/bin/python
# Classification (U)

"""Program:  movetofile_init.py

    Description:  Unit testing of MoveToFile.__init__ in isse_guard_class.py.

    Usage:
        test/unit/git_class/movetofile_init.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import isse_guard_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_review_with_sep -> Test with path seperator in review_dir.
        test_review_miss_sep -> Test with missing path seperator in review_dir.
        test_dissem_with_sep -> Test with path seperator in dissem_dir.
        test_dissem_miss_sep -> Test with missing path seperator in dissem_dir.
        test_init_default -> Test with default values set.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.fname = "File1.html"
        self.dissem_dir = "./test/unit/isse_guard_class/tmp"
        self.dissem_dir2 = "./test/unit/isse_guard_class/tmp/"
        self.file_path = os.path.join(self.dissem_dir, self.fname)
        self.review_dir = self.dissem_dir
        self.review_dir2 = self.dissem_dir + "/"

    def test_review_with_sep(self):

        """Function:  test_review_with_sep

        Description:  Test with path seperator in review_dir.

        Arguments:

        """

        isse = isse_guard_class.MoveToFile(self.file_path, self.review_dir2,
                                           self.dissem_dir)

        self.assertEqual((isse.cur_file_name, isse.cur_file_dir),
                         (self.fname, self.dissem_dir))

    def test_review_miss_sep(self):

        """Function:  test_review_miss_sep

        Description:  Test with missing path seperator in review_dir.

        Arguments:

        """

        isse = isse_guard_class.MoveToFile(self.file_path, self.review_dir,
                                           self.dissem_dir)

        self.assertEqual((isse.cur_file_name, isse.cur_file_dir),
                         (self.fname, self.dissem_dir))

    def test_dissem_with_sep(self):

        """Function:  test_dissem_with_sep

        Description:  Test with path seperator in dissem_dir.

        Arguments:

        """

        isse = isse_guard_class.MoveToFile(self.file_path, self.review_dir,
                                           self.dissem_dir2)

        self.assertEqual((isse.cur_file_name, isse.cur_file_dir),
                         (self.fname, self.dissem_dir))

    def test_dissem_miss_sep(self):

        """Function:  test_dissem_miss_sep

        Description:  Test with missing path seperator in dissem_dir.

        Arguments:

        """

        isse = isse_guard_class.MoveToFile(self.file_path, self.review_dir,
                                           self.dissem_dir)

        self.assertEqual((isse.cur_file_name, isse.cur_file_dir),
                         (self.fname, self.dissem_dir))

    def test_init_default(self):

        """Function:  test_init_default

        Description:  Test with default values set.

        Arguments:

        """

        isse = isse_guard_class.MoveToFile(self.file_path, self.review_dir,
                                           self.dissem_dir)

        self.assertEqual((isse.cur_file_name, isse.cur_file_dir),
                         (self.fname, self.dissem_dir))


if __name__ == "__main__":
    unittest.main()
