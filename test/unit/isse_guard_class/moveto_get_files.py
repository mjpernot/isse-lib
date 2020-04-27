#!/usr/bin/python
# Classification (U)

"""Program:  moveto_get_files.py

    Description:  Unit testing of MoveTo.get_files in isse_guard_class.py.

    Usage:
        test/unit/git_class/moveto_get_files.py

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
import mock

# Local
sys.path.append(os.getcwd())
import isse_guard_class
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_get_files_default -> Test with default values set.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dissem_dir = "./test/unit/isse_guard_class/tmp"
        self.file_list = []
        self.org = "EUCOM"
        self.dis_dir = self.dissem_dir + self.org + "/tape/IS"

    def test_get_files_default(self):

        """Function:  test_get_files_default

        Description:  Test with default values set.

        Arguments:

        """

        isse = isse_guard_class.MoveTo(self.dissem_dir)
        isse.get_files()

        self.assertEqual((isse.org, isse.dissem_dir, isse.file_list),
                         (self.org, self.dis_dir, self.file_list))


if __name__ == "__main__":
    unittest.main()
