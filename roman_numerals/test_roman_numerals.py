from nose.tools import assert_equals, assert_almost_equal
from roman_numerals import loaded


def test_loaded():
    assert loaded() == True
