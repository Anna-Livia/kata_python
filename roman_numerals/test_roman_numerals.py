from nose.tools import assert_equals, assert_almost_equal
from roman_numerals import to_roman_numeral

def test_1_gives_I():
    assert_equals(to_roman_numeral(1), "I")


def test_5_gives_V():
    assert_equals(to_roman_numeral(5), "V")


def test_10_gives_X():
    assert_equals(to_roman_numeral(10), "X")


def test_50_gives_L():
    assert_equals(to_roman_numeral(50), "L")


def test_100_gives_C():
    assert_equals(to_roman_numeral(100), "C")


def test_500_gives_D():
    assert_equals(to_roman_numeral(500), "D")


def test_1000_gives_M():
    assert_equals(to_roman_numeral(1000), "M")


def test_4_gives_IV():
    assert_equals(to_roman_numeral(4), "IV")
