from nose.tools import assert_equals, assert_almost_equal
from roman_numerals import loaded, to_roman_numeral


def test_loaded():
    assert loaded() == True


def test_1_gives_I():
    assert_equals(to_roman_numeral(1), "I")


def test_2_gives_II():
    assert_equals(to_roman_numeral(2), "II")


def test_4_gives_IV():
    assert_equals(to_roman_numeral(4), "IV")


def test_5_gives_V():
    assert_equals(to_roman_numeral(5), "V")
