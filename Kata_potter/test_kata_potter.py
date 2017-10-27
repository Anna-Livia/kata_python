from nose.tools import assert_equals, assert_almost_equal
from kata_potter import cash_register, bundle_finder


def test_no_sales_means_no_money():
    books = [0, 0]
    assert cash_register(books) == 0


def test_owe_1T1():
    books = [0, 1]
    assert cash_register(books) == 8


def test_owe_2T1_give_no_discount():
    books = [2, 0]
    assert_equals(cash_register(books), 2 * 8)


def test_1T1_and_1T2_return_2B1():
    assert bundle_finder([1, 1], 1) == (2, [])


def test_1T1_and_1T2_return_1B2():
    assert_equals(bundle_finder([2, 2], 2), (2, []))


def test_owe_1T1_and_1T2():
    books = [1, 1]
    assert_equals(cash_register(books), 2 * 8 * 0.95)


def test_2T1_and_1T2_return_3B1():
    assert bundle_finder([2, 1], 1) == (3, [])


def test_2T1_and_1T2_return_1B1_1B2():
    assert bundle_finder([2, 1], 2) == (1, [1])


def test_owe_2T1_and_1T2():
    books = [2, 1]
    assert_equals(cash_register(books), 2 * 8 * 0.95 + 8)

def test_1T1_1T2_1T3_return_3B1():
    assert bundle_finder([1, 1, 1], 1) == (3, [])


def test_1T1_1T2_1T3_return_1B2_1B1():
    assert_equals(bundle_finder([1, 1, 1], 2), (1, [1]))

def test_1T1_1T2_1T3_return_1B3():
    assert_equals(bundle_finder([1, 1, 1], 3), (1, []))

def test_owe_1T1_1T2_1T3():
    books = [1,1,1]
    assert_equals(cash_register(books), 3 * 8 * 0.9)


def test_owe_1T1_2T2_2T3():
    books = [1,2,2]
    assert_equals(cash_register(books), 3 * 8 * 0.9 + 2 * 8 * 0.95)


def test_owe_1T1_2T2_2T3_1T4():
    books = [1,2,2,1]
    assert_equals(cash_register(books), 4 * 8 * 0.8 + 2 * 8 * 0.95)

def final_test():
    assert_equals(cash_register([2, 2, 2, 1, 1]), 51.20)
