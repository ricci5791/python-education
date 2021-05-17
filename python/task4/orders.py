"""Module that contains order classes"""
import datetime
import uuid
from random import random
from typing import List

from menu import menu


class Order:
    """Contains functions for orders representation functionality"""
    menu = menu

    def __init__(self, item_list: List[str], customer: uuid):
        self.order_id = uuid.uuid4()
        self._item_list = None
        self.item_list = item_list
        self.order_time = datetime.datetime.now()
        self.price = self.calculate_price()
        self.customer = customer
        self.status = "Received"

    def calculate_price(self) -> float:
        """Calculates price based on chosen items"""
        price = 0.

        for item in self.item_list:
            price += self.menu.get(item)

        return price

    @property
    def item_list(self):
        """
        Property value of order price
        :return: Total price of a order
        """
        return self._item_list

    @item_list.setter
    def item_list(self, value: List[str]):
        for item in value:
            if item not in self.menu.keys():
                raise ValueError(f"Item doesn't exist: {item}")

        self._item_list = value

    def checkout(self) -> None:
        """Checkout order"""
        self.status = "Done"


class CarOrder(Order):
    """Implements car orders logics"""

    def __init__(self, *args, car_plate: str, pickup_line: int):
        """
        :param item_list: List of items that was ordered
        :param customer: ID of customer
        """
        super().__init__(*args)

        self.car_plate = car_plate
        self.pickup_line = pickup_line

    def deliver_to_car(self) -> bool:
        """Deliver order to a car of a customer"""

        delivery_res = random()
        if delivery_res < 0.95:
            self.checkout()
            return True
        else:
            print(f"Somethings went wrong, "
                  f"order {self.order_id} wasn't delivered")
            return False
