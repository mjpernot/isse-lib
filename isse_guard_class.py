# Classification (U)

"""Program:  isse_guard_class.py

    Description:  Class definitions and methods for ISSE Guard transfer use.

    Classes:
        IsseGuard
        MoveTo
            MoveToFile

"""

# Libraries and Global Variables

# Standard
import datetime
import os
import re

# Third-party
import xml.etree.ElementTree as ET

# Local
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class IsseGuard(object):

    """Class:  IsseGuard

    Description:  Class which is a representation of a ISSE Guard transfer.  A
        guard object is used as proxy to implement the transfer of documents
        from the a file location to an ISSE Guard system.

    Methods:
        __init__ -> Class instance initilization.
        set_other_files -> Adds additional files to be processed.

    """

    def __init__(self, network, cfg, action="process", files=None, keep=False,
                 **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the IsseGuard class.

        Arguments:
            (input) network -> Target network to transfer to.
            (input) cfg -> ISSE Guard configuration file.  With these options:
                dissem_dir -> Directory path to process pre-approved files.
                transfer_dir -> Directory path to process reviewed files.
                backup -> True | False - on whether to archive the files.
            (input) action -> Action to perform.  Default = process.
            (input) files -> File path or array of filepaths for sending.
            (input) keep -> Keep source files from files argument or delete
                them.  Default = False.

        """

        if isinstance(files, list):
            self.files = list(files)

        else:
            self.files = files

        # Contains directory structure for specified network enclave.
        network_target_dict = {
            "SIPR": "JWICStoSIPRtransfer",
            "BICES": "JWICStoBICEStransfer",
            "CW": "JWICStoCWtransfer"}

        # Contains the destination directory for specified network enclave.
        sftp_target_dict = {
            "SIPR": "outgoing/2_SIPR",
            "BICES": "outgoing/2_BICES",
            "CW": "outgoing/2_SG"}

        # File types to process for specified network enclave.  Inner
        #   dictionary determines MD5 hash creation and Base64 conversion for
        #   file type.
        file_types_dict = {
            "SIPR": {
                "*.zip": {"MD5": True, "Base64": False},
                "*.kmz": {"MD5": True, "Base64": True},
                "*.pptx": {"MD5": True, "Base64": True},
                "*.html": {"MD5": True, "Base64": False},
                "*_zip.64.txt": {"MD5": True, "Base64": False}},
            "BICES": {
                "*.zip": {"MD5": False, "Base64": False},
                "*.pdf": {"MD5": False, "Base64": False},
                "*metadata.xml": {"MD5": False, "Base64": False}},
            "CW": {
                "*.zip": {"MD5": True, "Base64": False},
                "*.kmz": {"MD5": True, "Base64": True},
                "*.pptx": {"MD5": True, "Base64": True},
                "*.html": {"MD5": True, "Base64": False},
                "*_zip.64.txt": {"MD5": True, "Base64": False}}}

        dtg = datetime.datetime.strftime(datetime.datetime.now(),
                                         "%Y%m%d-%H%M")
        year = datetime.datetime.strftime(datetime.datetime.now(), "%Y")
        month = datetime.datetime.strftime(datetime.datetime.now(), "%m")

        self.action = action
        self.network = network

        self.keep = keep

        self.name = "SERVICE-ISSE-TRANSFER-" + self.network + "-" + self.action

        if self.network in network_target_dict:
            self.target = network_target_dict[self.network]
            self.sftp_dir = sftp_target_dict[self.network]
            self.file_types = file_types_dict[self.network]

        else:
            raise ValueError("Invalid network selected: %s" % self.network)

        self.prog_log = cfg.log_dir + self.name + ".log"
        self.dissem_dir = cfg.dissem_dir
        self.transfer_dir = cfg.transfer_dir + self.target
        self.review_dir = self.transfer_dir + "/reviewed"
        self.complete_dir = self.transfer_dir + "/complete/" + year + "/" \
            + month
        self.job_log = self.review_dir + "/" + dtg + "-HPNEXTGEN-" \
            + self.target + "-LastRun.txt"

        status, err_msg = gen_libs.chk_crt_dir(self.complete_dir, create=True,
                                               write=True, read=True)

        if not status:
            raise OSError("Failed to create: %s\nReason:  %s"
                          % (self.complete_dir, err_msg))

        self.transfer_obj = ""
        self.other_files = []
        self.backup = cfg.backup
        self.other_file_types_dict = {}
        self.other_file_types = {}

    def set_other_files(self, add_to_list=None, **kwargs):

        """Method:  set_other_files

        Description:  Creates a dictionary of other/one-off files to be
            transferred.

        Arguments:
            (input)  add_to_list -> Additional files to be added to the array.

        """

        if add_to_list is None:
            add_to_list = []

        else:
            add_to_list = list(add_to_list)

        if self.network == "BICES":
            self.other_files = {}

        else:
            # Other and one-off files to be transferred, value is whether the
            #   file will be backed up during the process
            self.other_files = {
                self.review_dir + "/lookup.xml": False,
                self.review_dir + "/benumber_lookup.xml": False,
                "*-highpoint-app.zip": False}

            if self.network == "SIPR":
                self.other_files["*-IS-PULLED-*"] = True
                self.other_files["*-RELA-PULLED-*"] = True

            elif self.network == "CW":
                self.other_files["*-CW-PULLED-*"] = True
                self.other_files["SG-SERVER-PKI.zip"] = False

        # Other file types to process for specified network enclave, value is
        #   whether to make a MD5 hash for the file type.
        # NOTE:  The dictionary "keys" in self.other_file_types_dict must match
        #   what is in self.other_files for each network enclave.
        other_file_types_dict = {
            "SIPR": {
                self.review_dir + "/lookup.xml": True,
                self.review_dir + "/benumber_lookup.xml": True,
                "*-highpoint-app.zip": True,
                "*-IS-PULLED-*": True,
                "*-RELA-PULLED-*": True},
            "BICES": {},
            "CW": {
                self.review_dir + "/lookup.xml": True,
                self.review_dir + "/benumber_lookup.xml": True,
                "*-highpoint-app.zip": True,
                "*-CW-PULLED-*": True,
                "SG-SERVER-PKI.zip": True}}

        self.other_file_types = other_file_types_dict[self.network]

        for item in add_to_list:
            self.other_files[item] = False
            self.other_file_types[item] = True


class MoveTo(object):

    """Class:  MoveTo

    Description:  Class which is a representation of moving pre-approved
        documents to reviewed.  A MoveTo object is used as proxy to implement
        the moving of documents from the a file location to the reviewed
        directory.

    Methods:
        __init__ -> Class instance initilization.
        get_files -> Get list of files to be processed.

    """

    def __init__(self, dissem_dir, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the MoveTo class.

        Arguments:
            (input) dissem_dir -> Dissemination directory for new products.

        """

        # Only EUCOM is approved for pre-approved processing.
        self.org = "EUCOM"
        self.tape_dir = "IS"

        # XML Named spaces.
        self.ns = {"pubs": ".//{urn:us:gov:ic:pubs}",
                   "xlink": "{http://www.w3.org/1999/xlink}"}

        # Only these product lines are pre-approved for processing.
        self.product_list = ["Maritime Op Intel Brief"]

        # List of Dissemination Levels for processing.
        self.dissem_list = ["GEN-SCOL", "GEN-CW", "GEN-RELN", "GEN-USB",
                            "GEN-RELA"]

        self.dissem_dir = dissem_dir + self.org + "/tape/" + self.tape_dir
        self.file_list = []

    def get_files(self, **kwargs):

        """Method:  Get_Files

        Description:  Get list of html files to be processed.

        Arguments:

        """

        self.file_list = gen_libs.list_filter_files(self.dissem_dir, "*.html")


class MoveToFile(MoveTo):

    """Class:  MoveToFile

    Description:  Class which is a representation of a file instance in the
        moving pre-approved documents to reviewed.  A MoveToFile object is
        used as a proxy to implement the processing, checking, and moving of a
        file from a directory location to the reviewed directory.

    Methods:
        __init__ -> Class instance initilization.
        parse_xml_file -> Parse the XML file using ElementTree library.
        process_product -> Process product if meets product line requirements.
        add_to_zip -> Add file to zip list.
        add_to_cleanup -> Add file to cleanup list.

    """

    def __init__(self, file_path, review_dir, dissem_dir, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the MoveToFile class.

        Arguments:
            (input) file_path -> Directory path and file to be processed.
            (input) review_dir -> Review directory where file will be moved to.
            (input) dissem_dir -> Dissemination directory for new products.

        """

        super(MoveToFile, self).__init__(dissem_dir)

        self.cur_file_name = os.path.basename(file_path)
        self.cur_file_dir = os.path.dirname(file_path)

        if not self.dissem_dir.endswith(os.path.sep):
            self.dissem_dir = self.dissem_dir + os.path.sep

        if not review_dir.endswith(os.path.sep):
            review_dir = review_dir + os.path.sep

        self.zip_file_path = \
            review_dir + self.org + "-" + self.tape_dir \
            + "-" + re.sub("(?i)" + re.escape(".html"), ".zip",
                           self.cur_file_name)
        self.xml_file_path = re.sub("(?i)" + re.escape(".html"), ".xml",
                                    file_path)
        self.xml_file_name = os.path.basename(self.xml_file_path)
        self.dissem_level = ""
        self.object_id = ""
        self.xml_obj = None
        self.xml_obj_root = None
        self.images = []
        self.media = []
        self.files_to_zip = []
        self.cleanup_list = []

    def parse_xml_file(self, **kwargs):

        """Method:  parse_xml_file

        Description:  Parse the XML file using ElementTree library.

        Arguments:

        """

        self.xml_obj = ET.parse(self.xml_file_path)
        self.xml_obj_root = self.xml_obj.getroot()

        # Get list of all images.
        for parent in self.xml_obj_root.findall(self.ns["pubs"] +
                                                "StillImageExhibit"):
            child = parent.get(self.ns["xlink"] + "href")

            # Do not take any thumbnail images.
            if "-t.jpg" not in child:
                self.images.append(child)

        # Get list of all media entries.
        for parent in self.xml_obj_root.findall(self.ns["pubs"] +
                                                "OtherExhibit"):
            self.media.append(parent.get(self.ns["xlink"] + "href"))

        # Get the product line name.
        self.product_line = self.xml_obj_root.findall(self.ns["pubs"] +
                                                      "ProductLine")[0].text

    def process_product(self, **kwargs):

        """Method:  process_product

        Description:  Process the product if it meets product line
            requirements.

        Arguments:

        """

        if self.product_line in self.product_list:
            # Get document's dissemination level from file name.
            self.dissem_level = re.sub("-090109c.*.html", "",
                                       re.sub("[0-9]{8}-[0-9]{4}-", "",
                                              self.cur_file_name))

            # Get document ID from file name.
            self.object_id = "0901" + re.sub(".html", "",
                                             re.sub("[0-9]{8}-[0-9]{4}-.*0901",
                                                    "", self.cur_file_name))

    def add_to_zip(self, file_name, **kwargs):

        """Method:  add_to_zip

        Description:  Add file to zip list.

        Arguments:
            (input) file_name -> File name to add to zip list.

        """

        self.files_to_zip.append(file_name)

    def add_to_cleanup(self, file_name, **kwargs):

        """Method:  add_to_cleanup

        Description:  Add file to cleanup list.

        Arguments:
            (input) file_name -> File name to add to clean up list.

        """

        self.cleanup_list.append(file_name)
