# Python project that contains common libraries and classes for ISSE Guard.
# Classification (U)

# Description:
  Consists of a number of Python files that are common function libraries and classes for working with an ISSE Guard system.  These programs are not standalone programs, but are available for python programs to utilize.


###  This README file is broken down into the following sections:
 * Prerequisites
 * Installation
 * Program Description
 * Testing
   - Unit
   - Integration


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/gen_libs


# Installation:
  There are two types of installs: pip and git.

### Pip Installation:
  * Replace **{Other_Python_Project}** with the baseline path of another python program.

###### Create requirements file in another program's project to install isse-lib as a library module.

Create requirements-isse-lib.txt file:
```
vim {Other_Python_Project}/requirements-isse-lib.txt
```

Add the following lines to the requirements-isse-lib.txt file:
```
git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/isse-lib.git#egg=isse-lib
```

Create requirements-python-lib.txt file:
```
vim {Other_Python_Project}/requirements-python-lib.txt
```

Add the following lines to the requirements-python-lib.txt file:
```
git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/python-lib.git#egg=python-lib
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.
Modify the README.md file:
```
vim {Other_Python_Project}/README.md

Add the following lines under the "Install supporting classes and libraries" section.
```
   pip install -r requirements-sftp-lib.txt --target sftp_lib --trusted-host pypi.appdev.proj.coe.ic.gov
   pip install -r requirements-python-lib.txt --target sftp_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Git Installation:

Install general ISSE Guard libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/isse-lib.git
```

Install/upgrade system modules.

```
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries

```
cd isse-lib
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Program Descriptions:
### Program: isse_guard_class.py
##### Description: Class definitions and methods for ISSE Guard transfer use.
  * IsseGuard => Class which is a representation of a ISSE Guard transfer.
  * MoveTo => Class which is a representation of moving pre-approved documents to reviewed.
  * MoveToFile => Class which is a representation of a file instance in the moving pre-approved documents to reviewed.


# Testing:

# Unit Testing:

### Installation:

Install general ISSE Guard libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/isse-lib.git
```

Install/upgrade system modules.

```
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries

```
cd isse-lib
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Testing:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/isse-lib
test/unit/isse_guard_class/unit_test_run.sh
```

### Code Coverage:
```
cd {Python_Project}/isse-lib
test/unit/isse_guard_class/code_coverage.sh
```

# Integration Testing:

### Installation:

Install general ISSE Guard libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/isse-lib.git
```

Install/upgrade system modules.

```
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries

```
cd isse-lib
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Testing:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/isse-lib
test/integration/isse_guard_class/integration_test_run.sh
```

