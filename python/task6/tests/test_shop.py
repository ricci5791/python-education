"""Module contains tests for Shop and Product classes from to_test.py"""

import pytest

from python.task6 import to_test


@pytest.fixture(name="product_mock")
def fixture_product():
    """Mocks product instance with 'Title' and price 9.99"""
    return to_test.Product("Title", 9.99)


@pytest.mark.parametrize(
        "test_title, test_quantity, test_price, quantity_to_sub, expected", [
            ("Title", 5, 10, 10, 0),
            ("Title", 5, 20, 1, 19),
        ])
def test_product_subtraction(test_title, test_quantity, test_price,
                             quantity_to_sub,
                             expected):
    """
    Tests product quantity subtraction with correct data

    :param test_title: title of product
    :param test_quantity: quantity of product
    :param test_price: price of product
    :param quantity_to_sub: subtraction quantity
    :param expected: expected result
    :return: None
    """
    product = to_test.Product(test_title, test_quantity, test_price)

    product.subtract_quantity(quantity_to_sub)

    assert product.quantity == expected


@pytest.mark.parametrize(
        "test_title, test_quantity, test_price, quantity_to_sub, expected", [
            ("Title", 5, 10, [4, 6, 5], 0),
            ("Title", 5, 20, [4, 6, 5, 20], 0),
        ])
def test_product_subtraction_more_that_available(test_title, test_quantity,
                                                 test_price,
                                                 quantity_to_sub,
                                                 expected):
    """
    Tests if product correctly behaves with multiple quantities to be subtracted

    :param test_title: title of product
    :param test_quantity: quantity of product
    :param test_price: price of product
    :param quantity_to_sub: list of quantities to be subtracted
    :param expected: expected result
    :return: None
    """
    product = to_test.Product(test_title, test_quantity, test_price)

    for item in quantity_to_sub:
        product.subtract_quantity(item)

    assert product.quantity == expected


@pytest.mark.parametrize("new_price, expected", [
    (22.99, 22.99),
    (0.99, 0.99)
])
def test_product_change_price(product_mock, new_price, expected):
    """
    Tests changing price property to a new value

    :param product_mock: product fixture
    :param new_price: new price to be set
    :param expected: expected result
    :return: None
    """

    product_mock.change_price(new_price)
    assert product_mock.price == expected


@pytest.mark.parametrize("new_price", [
    (-22.99),
    (-0),
    "5.99",
    None,
])
def test_product_change_price_wrong_input(product_mock, new_price):
    """
    Tests changing price property with wrong type or value itself

    :param product_mock: product fixture
    :param new_price: wrong new price to be set
    :return:
    """

    product_mock.change_price(new_price)
    with pytest.raises(ValueError):
        product_mock.change_price(new_price)
        print(product_mock.price)
