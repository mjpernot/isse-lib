#!/usr/bin/python
# Classification (U)

"""Program:  movetofile_process_product.py

    Description:  Unit testing of MoveToFile.process_product in
        isse_guard_class.py.

    Usage:
        test/unit/git_class/movetofile_process_product.py

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
        test_product_not_in_list -> Test with product not in product_list.
        test_product_in_list -> Test with product in product_list.
        test_parse_xml_file_default -> Test with default values set.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.fname = "File1.html"
        self.dissem_dir = "./test/unit/isse_guard_class/tmp"
        self.file_path = os.path.join(self.dissem_dir, self.fname)
        self.review_dir = self.dissem_dir
        self.object_id = "0901File1"

    def test_product_not_in_list(self):

        """Function:  test_product_not_in_list

        Description:  Test with product not in product_list.

        Arguments:

        """

        isse = isse_guard_class.MoveToFile(self.file_path, self.review_dir,
                                           self.dissem_dir)
        isse.product_line = "Not in list"
        isse.process_product()

        self.assertEqual((isse.cur_file_name, isse.object_id),
                         (self.fname, ""))

    def test_product_in_list(self):

        """Function:  test_product_in_list

        Description:  Test with product in product_list.

        Arguments:

        """

        isse = isse_guard_class.MoveToFile(self.file_path, self.review_dir,
                                           self.dissem_dir)
        isse.product_line = "Maritime Op Intel Brief"
        isse.process_product()

        self.assertEqual((isse.cur_file_name, isse.object_id),
                         (self.fname, self.object_id))

    def test_parse_xml_file_default(self):

        """Function:  test_parse_xml_file_default

        Description:  Test with default values set.

        Arguments:

        """

        isse = isse_guard_class.MoveToFile(self.file_path, self.review_dir,
                                           self.dissem_dir)
        isse.product_line = "Maritime Op Intel Brief"
        isse.process_product()

        self.assertEqual((isse.cur_file_name, isse.object_id),
                         (self.fname, self.object_id))


if __name__ == "__main__":
    unittest.main()
