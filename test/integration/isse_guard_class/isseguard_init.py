#!/usr/bin/python
# Classification (U)

"""Program:  isseguard_init.py

    Description:  Integration testing of IsseGuard.__init__ in
        isse_guard_class.py.

    Usage:
        test/integration/git_class/isseguard_init.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import shutil

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

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
        test_files_list -> Test with list for files.
        test_files_string -> Test with string for files.
        test_files_empty_string -> Test with empty string for files.
        test_files_empty_list -> Test with empty list for files.
        test_files_not_passed -> Test with files not passed.
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

                self.log_dir = \
                    "./test/integration/isse_guard_class/tmp/log_dir"
                self.dissem_dir = \
                    "./test/integration/isse_guard_class/tmp/dissem_dir"
                self.transfer_dir = \
                    "./test/integration/isse_guard_class/tmp/transfer_dir"
                self.backup = True

        self.tmp_dir = "./test/integration/isse_guard_class/tmp"
        self.network_sipr = "SIPR"
        self.network_bices = "BICES"
        self.network_cw = "CW"
        self.network_other = "OTHER"
        self.cfg = CfgTest()
        self.action = "process"
        self.keep = True
        self.name = "SERVICE-ISSE-TRANSFER-SIPR-process"
        self.target = "JWICStoSIPRtransfer"
        self.prog_log = self.cfg.log_dir + self.name + ".log"
        self.review_dir = self.cfg.transfer_dir + self.target + "/reviewed"
        self.backup = self.cfg.backup
        self.files = ["DataFile1", "DataFile2"]

    def test_files_list(self):

        """Function:  test_files_list

        Description:  Test with list for files.

        Arguments:

        """

        isse = isse_guard_class.IsseGuard(self.network_sipr, self.cfg,
                                          files=self.files)

        self.assertEqual(isse.files, ["DataFile1", "DataFile2"])

    def test_files_string(self):

        """Function:  test_files_string

        Description:  Test with string for files.

        Arguments:

        """

        isse = isse_guard_class.IsseGuard(self.network_sipr, self.cfg,
                                          files="DataFile")

        self.assertEqual(isse.files, "DataFile")

    def test_files_empty_string(self):

        """Function:  test_files_empty_string

        Description:  Test with empty list for files.

        Arguments:

        """

        isse = isse_guard_class.IsseGuard(self.network_sipr, self.cfg,
                                          files="")

        self.assertEqual(isse.files, "")

    def test_files_empty_list(self):

        """Function:  test_files_empty_list

        Description:  Test with empty list for files.

        Arguments:

        """

        isse = isse_guard_class.IsseGuard(self.network_sipr, self.cfg,
                                          files=[])

        self.assertEqual(isse.files, [])

    def test_files_not_passed(self):

        """Function:  test_files_not_passed

        Description:  Test with files not passed.

        Arguments:

        """

        isse = isse_guard_class.IsseGuard(self.network_sipr, self.cfg)

        self.assertEqual(isse.files, None)

    def test_init_default(self):

        """Function:  test_init_default

        Description:  Test with default values set.

        Arguments:

        """

        isse = isse_guard_class.IsseGuard(self.network_sipr, self.cfg)

        self.assertEqual((isse.action, isse.name, isse.target, isse.prog_log,
                          isse.review_dir, isse.backup),
                         (self.action, self.name, self.target, self.prog_log,
                          self.review_dir, self.backup))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isdir(self.tmp_dir):
            shutil.rmtree(self.tmp_dir)


if __name__ == "__main__":
    unittest.main()
