#!/usr/bin/python
# Classification (U)

"""Program:  isseguard_init.py

    Description:  Unit testing of IsseGuard.__init__ in isse_guard_class.py.

    Usage:
        test/unit/git_class/isseguard_init.py

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

        self.network_sipr = "SIPR"
        self.network_bices = "BICES"
        self.network_cw = "CW"
        self.network_other = "OTHER"
        self.cfg = CfgTest()
        self.action = "process"
        self.files = "./test/unit/isse_guard_class/tmp"
        self.keep = True
        self.name = "SERVICE-ISSE-TRANSFER-SIPR-process"
        self.target = "JWICStoSIPRtransfer"
        self.prog_log = self.cfg.log_dir + self.name + ".log"
        self.review_dir = self.cfg.transfer_dir + self.target + "/reviewed"
        self.backup = self.cfg.backup

    @mock.patch("isse_guard_class.gen_libs.chk_crt_dir",
                mock.Mock(return_value=(True, None)))
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


if __name__ == "__main__":
    unittest.main()
