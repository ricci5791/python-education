"""Module contains tests for Shop and Product classes from to_test.py"""

import pytest

from python.task6 import to_test


@pytest.fixture(name="product_mock")
def fixture_product():
    """Mocks product instance with 'Title' and price 9.99"""
    return to_test.Product("Title", 9.99)


@pytest.fixture(name="empty_shop_mock")
def fixture_empty_shop():
    """Mocks shop instance with empty products list"""
    return to_test.Shop()


@pytest.fixture(name="filled_shop_mock")
def fixture_filled_shop():
    """Mocks shop instance with products list"""
    cheese = to_test.Product("Cheese", 29.99, 10)
    cream = to_test.Product("Cream", 10., 2)
    raspberry = to_test.Product("Raspberry", 5, 1)

    return to_test.Shop([cheese, cream, raspberry])


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


def test_shop_init(product_mock):
    """Tests creation of a shop with multiple products

    :param product_mock: product fixture
    :return: None
    """
    shop = to_test.Shop([product_mock] * 2)

    assert shop.products == [product_mock] * 2


@pytest.mark.parametrize("test_input", [
    "str",
    0.1,
    ["str", "str"]
])
def test_shop_init_wrong_input(test_input):
    """
    Tests if Shop init raises TyreError exception when product list type is
     wrong

    :param test_input: Wrong input
    :return: None
    """
    with pytest.raises(TypeError):
        to_test.Shop(test_input)


def test_shop_add_products(product_mock, empty_shop_mock):
    """
    Tests adding single product to the shop list

    :param product_mock: Fixture of Product
    :param empty_shop_mock: Fixture of Shop with empty products list
    :return: None
    """
    shop = empty_shop_mock

    shop.add_product(product_mock)

    assert product_mock in shop.products


@pytest.mark.parametrize("product_title, quantity", [
    ("Title", 5),
    ("Not existing", 1),
])
def test_shop_sell_product_product_not_exist(filled_shop_mock,
                                        product_title,
                                        quantity):
    """
    Tests selling of products that are not in products list of the shop

    :param filled_shop_mock: Fixture of Shop with products
    :param product_title: Title of non existing product
    :param quantity: Quantity to sell
    :return: None
    """
    assert filled_shop_mock.sell_product(product_title, quantity) is None


@pytest.mark.parametrize("product_title, quantity, expected", [
    ("Cheese", 2, 59.98),
    ("Cream", 1, 10),
    ("Raspberry", 1, 5),
])
def test_shop_sell_product_receipt_correct_input(filled_shop_mock,
                                                 product_title,
                                                 quantity, expected):
    """
    Tests how Shop calculates total price fro products

    :param filled_shop_mock: Fixture of filled shop
    :param product_title: Title of existing product
    :param quantity: Quantity of product to be sold
    :param expected: Expected result
    :return: None
    """
    assert filled_shop_mock.sell_product(product_title, quantity) == expected


@pytest.mark.parametrize("product_title, quantity", [
    ("Cheese", 11),
    ("Cream", 5),
    ("Raspberry", 5),
    ("Raspberry", -1),
])
def test_shop_sell_product_more_that_available(filled_shop_mock, product_title,
                                               quantity):
    """
    Tests how Shop responses when given product quantity is bigger that
    present in Shop

    :param filled_shop_mock: Fixture of filled shop
    :param product_title: Title of existing product
    :param quantity: Quantity of product to be sold
    :return: None
    """
    with pytest.raises(ValueError):
        filled_shop_mock.sell_product(product_title, quantity)


@pytest.mark.parametrize("product_list", [
    [("Cheese", 10),
     ("Cream", 2),
     ("Raspberry", 1)],
    [("Cheese", 5),
     ("Cheese", 5),
     ("Cream", 1),
     ("Cream", 1),
     ("Raspberry", 1)]
])
def test_shop_sell_product_delete_from_product_list(filled_shop_mock,
                                                    product_list):
    """
    Tests if after selling all the products Shop products is empty list

    :param filled_shop_mock: Fixture of filled shop
    :param product_list: List of products to be sold
    :return: None
    """

    for item, quantity in product_list:
        filled_shop_mock.sell_product(item, quantity)

    assert filled_shop_mock.products == []
