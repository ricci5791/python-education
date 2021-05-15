"""Module with implementation of restaurant class hierarchy """


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
        pass
