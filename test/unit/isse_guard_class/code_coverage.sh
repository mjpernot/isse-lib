#!/bin/bash
# Unit test code coverage for git_class.py module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=isse_guard_class test/unit/isse_guard_class/isseguard_init.py
coverage run -a --source=isse_guard_class test/unit/isse_guard_class/isseguard_set_other_files.py
coverage run -a --source=isse_guard_class test/unit/isse_guard_class/moveto_get_files.py
coverage run -a --source=isse_guard_class test/unit/isse_guard_class/moveto_init.py
coverage run -a --source=isse_guard_class test/unit/isse_guard_class/movetofile_init.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
