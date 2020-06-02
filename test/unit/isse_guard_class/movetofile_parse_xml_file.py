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
        test_multiple_media_find -> Test with multiple media find.
        test_no_media_find -> Test with no other media find.
        test_one_media_find -> Test with one other media find.
        test_thumbnail_image -> Test with thumbnail in file.
        test_multiple_images -> Test with multiple images.
        test_parse_xml_file_default -> Test with default values set.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.fname = "test.xml"
        self.fname2 = "test2.xml"
        self.fname3 = "test3.xml"
        self.fname4 = "test4.xml"
        self.fname5 = "test5.xml"
        self.fname6 = "test6.xml"
        self.dissem_dir = "./test/unit/isse_guard_class/basefiles"
        self.file_path = os.path.join(self.dissem_dir, self.fname)
        self.file_path2 = os.path.join(self.dissem_dir, self.fname2)
        self.file_path3 = os.path.join(self.dissem_dir, self.fname3)
        self.file_path4 = os.path.join(self.dissem_dir, self.fname4)
        self.file_path5 = os.path.join(self.dissem_dir, self.fname5)
        self.file_path6 = os.path.join(self.dissem_dir, self.fname6)
        self.review_dir = self.dissem_dir
        self.images = ["image_name.jpg"]
        self.images2 = ["image_name1.jpg", "image_name2.jpg"]
        self.media = ["pdf_file.pdf"]
        self.media2 = ["pdf_file.pdf", "pdf_file2.pdf"]

    def test_multiple_media_find(self):

        """Function:  test_multiple_media_find

        Description:  Test with multiple media find.

        Arguments:

        """

        isse = isse_guard_class.MoveToFile(self.file_path6, self.review_dir,
                                           self.dissem_dir)
        isse.ns = {"pubs": "pubs",
                   "xlink": "xlink"}
        isse.parse_xml_file()

        self.assertEqual((isse.cur_file_name, isse.cur_file_dir, isse.media),
                         (self.fname6, self.dissem_dir, self.media2))

    def test_no_media_find(self):

        """Function:  test_no_media_find

        Description:  Test with no other media find.

        Arguments:

        """

        isse = isse_guard_class.MoveToFile(self.file_path5, self.review_dir,
                                           self.dissem_dir)
        isse.ns = {"pubs": "pubs",
                   "xlink": "xlink"}
        isse.parse_xml_file()

        self.assertEqual((isse.cur_file_name, isse.cur_file_dir, isse.media),
                         (self.fname5, self.dissem_dir, []))

    def test_one_media_find(self):

        """Function:  test_one_media_find

        Description:  Test with one other media find.

        Arguments:

        """

        isse = isse_guard_class.MoveToFile(self.file_path4, self.review_dir,
                                           self.dissem_dir)
        isse.ns = {"pubs": "pubs",
                   "xlink": "xlink"}
        isse.parse_xml_file()

        self.assertEqual((isse.cur_file_name, isse.cur_file_dir, isse.media),
                         (self.fname4, self.dissem_dir, self.media))

    def test_thumbnail_image(self):

        """Function:  test_thumbnail_image

        Description:  Test with thumbnail in file.

        Arguments:

        """

        isse = isse_guard_class.MoveToFile(self.file_path3, self.review_dir,
                                           self.dissem_dir)
        isse.ns = {"pubs": "pubs",
                   "xlink": "xlink"}
        isse.parse_xml_file()

        self.assertEqual((isse.cur_file_name, isse.cur_file_dir, isse.images),
                         (self.fname3, self.dissem_dir, self.images2))

    def test_multiple_images(self):

        """Function:  test_multiple_images

        Description:  Test with multiple images.

        Arguments:

        """

        isse = isse_guard_class.MoveToFile(self.file_path2, self.review_dir,
                                           self.dissem_dir)
        isse.ns = {"pubs": "pubs",
                   "xlink": "xlink"}
        isse.parse_xml_file()

        self.assertEqual((isse.cur_file_name, isse.cur_file_dir, isse.images),
                         (self.fname2, self.dissem_dir, self.images2))

    def test_parse_xml_file_default(self):

        """Function:  test_parse_xml_file_default

        Description:  Test with default values set.

        Arguments:

        """

        isse = isse_guard_class.MoveToFile(self.file_path, self.review_dir,
                                           self.dissem_dir)
        isse.ns = {"pubs": "pubs",
                   "xlink": "xlink"}
        isse.parse_xml_file()

        self.assertEqual((isse.cur_file_name, isse.cur_file_dir, isse.images),
                         (self.fname, self.dissem_dir, self.images))


if __name__ == "__main__":
    unittest.main()
