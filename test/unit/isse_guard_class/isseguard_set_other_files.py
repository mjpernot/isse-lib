#!/usr/bin/python
# Classification (U)

"""Program:  isseguard_set_other_files.py

    Description:  Unit testing of IsseGuard.set_other_files in
        isse_guard_class.py.

    Usage:
        test/unit/git_class/isseguard_set_other_files.py

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
        test_network_bices -> Test with network set to bices.
        test_network_cw -> Test with network set to cw.
        test_network_sipr -> Test with network set to sipr.
        test_add_to_list_two -> Test with add_to_list with two items.
        test_add_to_list_one -> Test with add_to_list with one item.
        test_add_to_list_empty -> Test with add_to_list as empty list.
        test_add_to_list_none -> Test with add_to_list is not passed.
        test_init_default -> Test with default values set.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        class CfgTest(object):

            """Class:  CfgTest

            Description:  Class which is a representation of a cfg module.

            Methods:
                __init__ -> Initialize configuration environment.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the CfgTest class.

                Arguments:

                """

                self.log_dir = "./test/unit/isse_guard_class/tmp/log_dir"
                self.dissem_dir = "./test/unit/isse_guard_class/tmp/dissem_dir"
                self.transfer_dir = \
                    "./test/unit/isse_guard_class/tmp/transfer_dir"
                self.backup = True

        self.lookup = "/lookup.xml"
        self.benumber = "/benumber_lookup.xml"
        self.hp_app = "*-highpoint-app.zip"
        self.network_sipr = "SIPR"
        self.network_bices = "BICES"
        self.network_cw = "CW"
        self.network_other = "OTHER"
        self.cfg = CfgTest()
        self.action = "process"
        self.files = "./test/unit/isse_guard_class/tmp"
        self.keep = True

        self.target = "JWICStoSIPRtransfer"
        self.target2 = "JWICStoCWtransfer"
        self.target3 = "JWICStoBICEStransfer"
        self.name = "SERVICE-ISSE-TRANSFER-SIPR-process"
        self.prog_log = self.cfg.log_dir + self.name + ".log"
        self.review_dir = self.cfg.transfer_dir + self.target + "/reviewed"
        self.other_file_types = {
            self.review_dir + self.lookup: True,
            self.review_dir + self.benumber: True,
            self.hp_app: True,
            "*-IS-PULLED-*": True,
            "*-RELA-PULLED-*": True}
        self.other_files = {
            self.review_dir + self.lookup: False,
            self.review_dir + self.benumber: False,
            self.hp_app: False,
            "*-IS-PULLED-*": True,
            "*-RELA-PULLED-*": True}
        self.add_to_list = ["One"]
        self.add_to_list2 = list(self.add_to_list)
        self.add_to_list2.append("Two")
        self.other_files2 = dict(self.other_files)
        self.other_file_types2 = dict(self.other_file_types)
        self.other_files2["One"] = False
        self.other_file_types2["One"] = True
        self.other_files3 = dict(self.other_files2)
        self.other_file_types3 = dict(self.other_file_types2)
        self.other_files3["Two"] = False
        self.other_file_types3["Two"] = True
        self.review_dir2 = self.cfg.transfer_dir + self.target2 + "/reviewed"
        self.other_file_types4 = {
            self.review_dir2 + self.lookup: True,
            self.review_dir2 + self.benumber: True,
            self.hp_app: True,
            "*-CW-PULLED-*": True,
            "SG-SERVER-PKI.zip": True}
        self.other_files4 = {
            self.review_dir2 + self.lookup: False,
            self.review_dir2 + self.benumber: False,
            self.hp_app: False,
            "*-CW-PULLED-*": True,
            "SG-SERVER-PKI.zip": False}
        self.other_file_types5 = {}
        self.other_files5 = {}

    @mock.patch("isse_guard_class.gen_libs.chk_crt_dir",
                mock.Mock(return_value=(True, None)))
    def test_network_bices(self):

        """Function:  test_network_bices

        Description:  Test with network set to bices.

        Arguments:

        """

        isse = isse_guard_class.IsseGuard(self.network_bices, self.cfg)
        isse.set_other_files()

        self.assertEqual((isse.other_files, isse.other_file_types),
                         (self.other_files5, self.other_file_types5))

    @mock.patch("isse_guard_class.gen_libs.chk_crt_dir",
                mock.Mock(return_value=(True, None)))
    def test_network_cw(self):

        """Function:  test_network_cw

        Description:  Test with network set to cw.

        Arguments:

        """

        isse = isse_guard_class.IsseGuard(self.network_cw, self.cfg)
        isse.set_other_files()

        self.assertEqual((isse.other_files, isse.other_file_types),
                         (self.other_files4, self.other_file_types4))

    @mock.patch("isse_guard_class.gen_libs.chk_crt_dir",
                mock.Mock(return_value=(True, None)))
    def test_network_sipr(self):

        """Function:  test_network_sipr

        Description:  Test with network set to sipr.

        Arguments:

        """

        isse = isse_guard_class.IsseGuard(self.network_sipr, self.cfg)
        isse.set_other_files()

        self.assertEqual((isse.other_files, isse.other_file_types),
                         (self.other_files, self.other_file_types))

    @mock.patch("isse_guard_class.gen_libs.chk_crt_dir",
                mock.Mock(return_value=(True, None)))
    def test_add_to_list_two(self):

        """Function:  test_add_to_list_two

        Description:  Test with add_to_list with two items.

        Arguments:

        """

        isse = isse_guard_class.IsseGuard(self.network_sipr, self.cfg)
        isse.set_other_files(add_to_list=self.add_to_list2)

        self.assertEqual((isse.other_files, isse.other_file_types),
                         (self.other_files3, self.other_file_types3))

    @mock.patch("isse_guard_class.gen_libs.chk_crt_dir",
                mock.Mock(return_value=(True, None)))
    def test_add_to_list_one(self):

        """Function:  test_add_to_list_one

        Description:  Test with add_to_list with one item.

        Arguments:

        """

        isse = isse_guard_class.IsseGuard(self.network_sipr, self.cfg)
        isse.set_other_files(add_to_list=self.add_to_list)

        self.assertEqual((isse.other_files, isse.other_file_types),
                         (self.other_files2, self.other_file_types2))

    @mock.patch("isse_guard_class.gen_libs.chk_crt_dir",
                mock.Mock(return_value=(True, None)))
    def test_add_to_list_empty(self):

        """Function:  test_add_to_list_empty

        Description:  Test with add_to_list as empty list.

        Arguments:

        """

        isse = isse_guard_class.IsseGuard(self.network_sipr, self.cfg)
        isse.set_other_files(add_to_list=[])

        self.assertEqual((isse.other_files, isse.other_file_types),
                         (self.other_files, self.other_file_types))

    @mock.patch("isse_guard_class.gen_libs.chk_crt_dir",
                mock.Mock(return_value=(True, None)))
    def test_add_to_list_none(self):

        """Function:  test_add_to_list_none

        Description:  Test with add_to_list is not passed.

        Arguments:

        """

        isse = isse_guard_class.IsseGuard(self.network_sipr, self.cfg)
        isse.set_other_files()

        self.assertEqual((isse.other_files, isse.other_file_types),
                         (self.other_files, self.other_file_types))

    @mock.patch("isse_guard_class.gen_libs.chk_crt_dir",
                mock.Mock(return_value=(True, None)))
    def test_set_other_files_default(self):

        """Function:  test_set_other_files_default

        Description:  Test with default values set.

        Arguments:

        """

        isse = isse_guard_class.IsseGuard(self.network_sipr, self.cfg)
        isse.set_other_files()

        self.assertEqual((isse.other_files, isse.other_file_types),
                         (self.other_files, self.other_file_types))


if __name__ == "__main__":
    unittest.main()
