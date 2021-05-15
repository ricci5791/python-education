"""Module with implementation of restaurant class hierarchy """
from datetime import datetime


class Food:
    """
    Contains functions for food representation
    functionality and used in Storage
    """

    def __init__(self, name: str, avg_mass: float, expire_time: datetime):
        self.name = name
        self.avg_mass = avg_mass
        self.expire_time = expire_time

    def check_expire(self) -> bool:
        """Checks if item is expired"""
        return self.expire_time < datetime.now()


class Storage:
    """
    Contains functions for food storing
    functionality and used in HallDispatcher
    """

    def __init__(self):
        self.temperature = 0.0
        self.goods = dict()
        self._storage_conditions = dict()

    def reserve_food(self, food_list: list[tuple[str, float]]) -> bool:
        """
        Takes list of goods to be reserved and do it if possible
        "param food_list: List of good to be reserved, name and quantity
        """

    def get_invoice(self, food_list: list[str, float]) -> bool:
        """Add given quantity of goods in the list to the storage"""

    def write_off_food(self, food_list: list[str]) -> None:
        """Checks expiration time of goods and delete them if expired"""


class HallDispatcher:
    """Contains functions for hall functionality and used in Restaurant"""

    def __init__(self):
        self.workers_list = list()
        self.orders_list = list()
        self.storage = None


class Restaurant:
    """Class with restaurant functionality"""

    def __init__(self):
        self.__total_money_flow = 0.0
        self.hall_dispatcher = HallDispatcher()
        self.problems_list = list()
        self.is_closed = True

    def get_statistics(self) -> str:
        """
        Returns generated statistic about restaurant operations
        in string representation
        """
        return f"{self.__total_money_flow}"

    def get_transactions_history(self, period: tuple[str, str]) \
            -> list[tuple[str, float]]:
        """Returns list of timestamp and total bill charged
        :param period: Tuple of 2 timestamps that bound some time period"""
