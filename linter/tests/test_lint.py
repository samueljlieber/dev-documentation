from pathlib import Path

from sphinxlint import paragraphs

import pytest

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from sphinxlint import main as mainsphinx

from main import main

FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures"

@pytest.mark.parametrize("file", [str(f) for f in (FIXTURE_DIR / "xpass").iterdir()])
def test_sphinxlint_shall_pass(file, capsys):
    has_errors = main(["main.py", "--enable", "all", str(file)])
    out, err = capsys.readouterr()
    assert err == ""
    assert out == "No problems found.\n"
    assert not has_errors

def gather_xfail():
    """Find all rst files in the fixtures/xfail directory.

    Each file is searched for lines containing expcted errors, they
    are starting with `.. expect: `.
    """
    marker = ".. expect: "
    for file in (FIXTURE_DIR / "xfail").iterdir():
        expected_errors = []
        for line in Path(file).read_text(encoding="UTF-8").splitlines():
            if line.startswith(marker):
                expected_errors.append(line[len(marker) :])
        yield str(file), expected_errors


@pytest.mark.parametrize("file,expected_errors", gather_xfail())
def test_sphinxlint_shall_not_pass(file, expected_errors, capsys):
    has_errors = main(["main.py", "--enable", "all", file])
    out, err = capsys.readouterr()
    assert out != "No problems found.\n"
    assert err == ""
    assert has_errors
    assert expected_errors, (
        "Specify expected errors, "
        """add one using a ".. expect: " line."""
    )
    for expected_error in expected_errors:
        assert expected_error in out
    number_of_expected_errors = len(expected_errors)
    number_of_reported_errors = len(out.splitlines())
    assert number_of_expected_errors == number_of_reported_errors
