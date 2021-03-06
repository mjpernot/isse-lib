#!/usr/bin/python
# Classification (U)

"""Program:  movetofile_add_to_zip.py

    Description:  Unit testing of MoveToFile.add_to_zip in
        isse_guard_class.py.

    Usage:
        test/unit/git_class/movetofile_add_to_zip.py

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
        test_parse_xml_file_default -> Test with default values set.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.fname = "File1.html"
        self.fname2 = "File2.html"
        self.dissem_dir = "./test/unit/isse_guard_class/tmp"
        self.file_path = os.path.join(self.dissem_dir, self.fname)
        self.review_dir = self.dissem_dir
        self.files_to_zip = [self.fname2]

    def test_parse_xml_file_default(self):

        """Function:  test_parse_xml_file_default

        Description:  Test with default values set.

        Arguments:

        """

        isse = isse_guard_class.MoveToFile(self.file_path, self.review_dir,
                                           self.dissem_dir)
        isse.add_to_zip(self.fname2)

        self.assertEqual((isse.files_to_zip), (self.files_to_zip))


if __name__ == "__main__":
    unittest.main()
