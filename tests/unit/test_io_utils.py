"""Test suite for test_io_utils.py"""
import os
import pytest
from assignment4.io_utils import get_filehandle
import gene_names_from_chr21
import find_common_cats
# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_filehandle_for_OSError
# " doesn't conform to snake_case naming style"
# pylint: disable=C0103
import intersection_of_gene_names

FILE_TO_TEST = "chr21_genes.txt"
FILE_TO_TEST_INPUT = " "
FILE_TO_TEST_FIND_COMMON_CATS = "categories.txt"
FILE_TO_TEST_INTERSECTION_OF_GENE_NAMES = "intersection_output.txt"


def test_get_gene_symbol():
    line = "A1BG	alpha-1-B glycoprotein"
    result = intersection_of_gene_names.get_gene_symbol(line)
    assert result, "A1BG"


def test_reading_textfile_into_dict():
    test_file = get_filehandle(file=FILE_TO_TEST, mode="r")
    d = gene_names_from_chr21.reading_textfile_into_dict(test_file)
    assert len(d), 285
    test_file.close()


def test_gene_count():
    test_file = get_filehandle(file=FILE_TO_TEST, mode="r")
    d = find_common_cats.gene_count(test_file)
    assert d["1.1"], 103
    assert d["5"], 59
    test_file.close()


def test_store_the_description():
    test_file = get_filehandle(file="chr21_genes_categories.txt", mode="r")
    d = find_common_cats.store_the_description(test_file)
    assert d["3.2"], "Genes with amino-acid similarity confined to regions of a known protein without known " \
                     "functional association. "
    test_file.close()


def test_existing_get_filehandle_for_reading():
    test = get_filehandle(file=FILE_TO_TEST, mode="r")
    assert hasattr(test, "read") is True, "Not able to open for writing"
    test.close()
    os.remove(FILE_TO_TEST)


def test_existing_get_filehandle_for_writing():
    # does it open a file for writing
    # test
    test = get_filehandle(file=FILE_TO_TEST, mode="w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove(FILE_TO_TEST)


def test_get_filehandle_for_OSError():
    # does it raise OSError
    # this should exit
    with pytest.raises(OSError):
        get_filehandle("does_not_exist.txt", "r")


def _create_file_for_testing():
    pass


def test_get_filehandle_for_ValueError():
    # does it raise ValueError
    # this should exit
    _create_file_for_testing()
    with pytest.raises(ValueError):
        get_filehandle("does_not_exist.txt", "rrr")
        os.remove(FILE_TO_TEST)
