#!/usr/bin/python
# Classification (U)

"""Program:  movetofile_parse_xml_file.py

    Description:  Unit testing of MoveToFile.parse_xml_file in
        isse_guard_class.py.

    Usage:
        test/unit/git_class/movetofile_parse_xml_file.py

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

        self.fname = "test.xml"
        self.dissem_dir = "./test/unit/isse_guard_class/basefiles"
        self.file_path = os.path.join(self.dissem_dir, self.fname)
        self.review_dir = self.dissem_dir

    @unittest.skip("Error:  Require xml file to test with")
    def test_parse_xml_file_default(self):

        """Function:  test_parse_xml_file_default

        Description:  Test with default values set.

        Arguments:

        """

        isse = isse_guard_class.MoveToFile(self.file_path, self.review_dir,
                                           self.dissem_dir)
        isse.parse_xml_file()

        self.assertEqual((isse.cur_file_name, isse.cur_file_dir),
                         (self.fname, self.dissem_dir))


if __name__ == "__main__":
    unittest.main()
