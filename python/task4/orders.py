"""Module that contains order classes"""
import datetime
import uuid


class Order:
    """Contains functions for orders representation functionality"""

    def __init__(self, item_list: list[str], customer: uuid):
        self.order_id = uuid.uuid4()
        self.item_list = item_list
        self.order_time = datetime.datetime.now()
        self.price = self.calculate_price(item_list)
        self.customer = customer
        self.status = "Received"

    def calculate_price(self, item_list: list[str]) -> float:
        """Calculates price based on chosen items"""
        return 0.0

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
