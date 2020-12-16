# test HW01: Copy Rename Delete
# 4 points

# NOTE: run from the top of the repository. The directory "PHY494" should
#       be visible in the current directory when the tests are run.
#
#       On the command line:
#
#          cd hw01
#          pytest
#
#       should run all the tests in the hw01/tests directory.

import pytest
import pathlib

@pytest.fixture(scope="module")
def tree():
    top = pathlib.Path('PHY494/01_shell')
    Documents = top / "Documents"
    work = Documents / "work"
    data = top / "data"
    notes = data / "notes"
    work_files = [work / fn for fn in ("TODO.bak", "TODO.txt", "hints.txt", "lesson.txt")]
    notes_files = [notes / "TODO.txt"]
    files = {"directories": [top, Documents, work, data, notes],
             "files": work_files + notes_files,
             }
    return files

def test_top_dir(tree):
    top = tree["directories"][0]
    assert top.is_dir(), f"Directory '{top}' is missing"

def test_all_dirs(tree):
    for directory in tree["directories"]:
        assert directory.is_dir(), f"Directory '{directory}' is missing or not a directory!"

def test_all_files(tree):
    for filepath in tree["files"]:
        assert filepath.is_file(), f"File '{filepath}' is missing or not a file!"

