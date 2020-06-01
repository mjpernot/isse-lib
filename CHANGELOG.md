# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [3.1.2] - 2020-04-27
### Fixed
- IsseGuard.\_\_init\_\_:  Fixed problem with mutable default arguments issue.
- IsseGuard.set_other_files:  Fixed problem with mutable default arguments issue.

### Changed
- Documentation updates.


## [3.1.1] - 2018-11-02
### Fixed
- IsseGuard.set_other_files:  Changed default mutable type in argument list to "None" and set the variable to a list inside the method.

### Changed
- Documentation updates.


## [3.1.0] - 2018-09-12
### Changed
- IsseGuard.\_\_init\_\_:  Turn off MD5 creation for "BICES".

### Removed
- Isse_Guard:  Class was previously deprecated.
- Move_To_File:  Class was previously deprecated.
- Move_To:  Class was previously deprecated.


## [3.0.1] - 2018-04-19
### Changed
- Documentation updates.


## [3.0.0] - 2018-04-19
Breaking Change

### Added
- IsseGuard class:  Replaces Isse_Guard class.
- MoveTo class:  Replaces Move_To class.
- MoveToFile class:  Replaces Move_To_File class.

### Deprecated
- Isse_Guard class:  Replaced by IsseGuard class.
- Move_To class:  Replaced by MoveTo class.
- Move_To_File class:  Replaced by MoveToFile class.

### Changed
- Changed "gen_libs" calls to new naming schema.
- IsseGuard.\_\_init\_\_:  Replaced gen_libs.Chk_Crt_Dir with gen_libs.chk_crt_dir call, also refactored logic checking code.
- Setup single-source version control.


## [2.1.0] - 2018-04-19
### Added
- Added single-source version control.


## [2.0.0] - 2017-10-23
Breaking Change

### Change
- Add ability to convert certain file types to base64 format.
- ISSE_Guard.\_\_init\_\_:  Change file_types_dict from dictionary to dictionary within a dictionary.  Each file type will have a dictionary to determine if MD5 creation or base64 conversion will occur.


## [1.2.1] - 2017-09-27
### Fixed
- other_files does not have capability to create MD5 files as there is no value setting for them.
- ISSE_Guard.\_\_init\_\_:  Add other_file_types and other_file_types_dict attributes.
- ISSE_Guard.set_other_files:  Initialize other_file_types and other_file_types_dict attributes.


## [1.2.0] - 2017-09-25
### Changed
- Isse_Guard.set_other_files:  Remove .64.txt from other_files as it will be covered under file_types_dict attribute as _zip.64.txt file type.
- Isse_Guard.\_\_init\_\_:  Add \_zip.64.txt to file_types_dict for SIPR and CW - to allow the processing of the file type.  Change all file types to True to allow MD5 creation.


## [1.1.0] - 2017-09-21
### Changed
- Isse_Guard.set_other_files:  Add \*.64.txt to other_files attributes - to allow base64 text files to be processed for SIPR and CW.


## [1.0.1] - 2017-08-03
### Fixed
- Rename List_Files to List_Filter_Files due to duplicate function name in gen_libs library.
- Move_To.get_files:  Rename List_Files to List_Filter_Files.


## [1.0.0] - 2017-07-31
- General release.


## [0.3.1] - 2017-07-25
### Changed
- Isse_Guard.\_\_init\_\_:  Add self.action to self.name to individualize log names.


## [0.3.0] - 2017-07-25
- Field test release.


## [0.2.0] - 2017-07-25
- Beta release.


## [0.1.0] - 2017-07-11
- Alpha release.

