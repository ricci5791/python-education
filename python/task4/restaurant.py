"""Module with implementation of restaurant class hierarchy """
import random
import uuid
import datetime as dt
from typing import List, Tuple, Dict

from orders import Order
from people import Cook, Manager, Customer

ReservingFoodList = Dict[str, float]
InvoiceFoodList = List[Tuple[str, int]]
PeriodBoundaries = List[dt.datetime]
TransactionHistory = List[Tuple[str, float]]


class Food:
    """
    Contains functions for food representation
    functionality and used in Storage
    """

    def __init__(self, name: str, quantity: float, expire_time: dt.datetime):
        self.name = name
        self.quantity = quantity
        self.expire_time = expire_time

    def check_expire(self) -> bool:
        """Checks if item is expired"""
        return self.expire_time < dt.datetime.now()

    def __eq__(self, other):
        return self.name == other

    def __iadd__(self, other):
        self.quantity += other
        return self

    def __isub__(self, other):
        self.quantity -= other
        return self

    def __lt__(self, other):
        return self.quantity < other

    def __str__(self):
        return f"{self.name}: {self.quantity} units. " \
               f"Expires at {self.expire_time}"

    def __repr__(self):
        return f"{self.name}:{self.quantity}; exp:{self.expire_time}"


class Storage:
    """
    Contains functions for food storing
    functionality and used in HallDispatcher
    """
    storage_conditions = dict()

    def __init__(self):
        self.temperature = 0.0
        self.goods = dict()

    def reserve_food(self, food_list: ReservingFoodList) -> bool:
        """
        Takes list of goods to be reserved and do it if possible
        :param food_list: List of good to be reserved, name and quantity
        """
        for food, quantity in food_list.items():
            if self.goods.get(food) is None or self.goods.get(food) \
                    < quantity:
                return False

        for food, quantity in food_list.items():
            self.goods[food] -= quantity

        return True

    def get_invoice(self, food_list: InvoiceFoodList) -> bool:
        """Add given quantity of goods in the list to the storage"""
        for food, quantity in food_list:
            if food in self.goods:
                self.goods[food] += quantity
            else:
                self.goods[food] = Food(food,
                                        quantity,
                                        dt.datetime.strptime("18/09/21",
                                                             "%d/%m/%y"))

        return True

    def write_off_food(self, food_list: List[str] = None) -> None:
        """Checks expiration time of goods and delete them if expired"""
        if food_list is None:
            food_list = self.goods

        for food in food_list.copy():
            if food in self.goods.keys() and self.goods.get(food) \
                    .check_expire():
                self.goods.pop(food)


class HallDispatcher:
    """Contains functions for hall functionality and used in Restaurant"""

    def __init__(self):
        self.workers_list = list()
        self.orders_list = list()
        self.storage = None
        self.customers = list()

    def __search_order(self, order_id: uuid) -> Order:
        """
        Search for given order by ID and return it
        :param order_id: Order id to be searched
        :return: Order or None if doesn't exist
        :rtype: Order or None
        """
        for order_item in self.orders_list:
            if order_item.order_id == order_id:
                return order_item
        return None

    def __search_cook(self, order_id: uuid) -> bool:
        """
        Search for available cook to cook given meal
        :param order_id: Order meal to be cooked
        :return: True if cook is available, False otherwise
        :rtype: bool
        """
        order = self.__search_order(order_id)

        if order is None:
            print("Such order doesn't exist")
            return False

        for cook in self.workers_list:
            if isinstance(cook, Cook) and cook.current_meal is None:
                cook.start_cooking(order.item_list)
                return True

        return False

    def make_order(self) -> None:
        """
        Make random customer make a order with random meal from menu
        :return: None
        """
        customer = random.choice(self.customers)

        order = customer.make_order()
        self.orders_list.append(order)

        if self.__search_cook(order.order_id):
            order.status = "Done"

    def abort_order(self, order_id: uuid) -> None:
        """
        Set given order status to be 'Aborted'
        :param order_id: Order id to set changed
        :return: None
        """
        order = self.__search_order(order_id)
        if order is not None:
            order.status = "Aborted"

    def return_orders(self) -> List[Order]:
        """Return list of orders that was made
        :return: List of orders
        :rtype: List[Order]"""
        return self.orders_list

    def add_customer(self):
        """Create random customer to the hall"""
        customer = Customer("Billy", "Soprano")

        self.customers.append(customer)

    def done_orders_count(self) -> int:
        """
        Counts number of done orders
        :return: Number of done orders
        :rtype: int
        """
        counter = 0

        for order in self.orders_list:
            if order.status == "Done":
                counter += 1

        return counter

    def get_service_rate(self) -> int:
        """
        Give service rating from one of the managers
        :return: Service rate
        :rtype: int
        """
        for worker in self.workers_list:
            if isinstance(worker, Manager):
                return worker.get_customer_service_rate()
        return None


class Problem:
    """Contains compliance functionality and used in Restaurant"""

    def __init__(self, topic: str, explanation: str, manager: Manager = None):
        self.problem_id = uuid.uuid4()
        self.topic = topic
        self.explanation = explanation
        self.date = dt.datetime.now()
        self.handler_manager = manager
        self.status = "Received"

    def solve_problem(self) -> bool:
        """Try to solve problem
        :return: Boolean whether problem been solved"""
        if self.handler_manager.solve_order_problem(self):
            self.status = "Solved"
            return True
        return False

    def suppress_problem(self) -> bool:
        """Try to solve problem
        :return: Boolean whether problem been solved"""
        self.status = f"Suppressed at {dt.datetime.now()}"
        return True


class Restaurant:
    """Class with restaurant functionality"""

    def __init__(self):
        self.hall_dispatcher = HallDispatcher()
        self.__total_money_flow = self.__calculate_money_flow()
        self.problems_list = list()
        self.is_closed = True

    def __calculate_money_flow(self):
        money_flow = 0.0
        for order in self.hall_dispatcher.orders_list:
            money_flow += order.price
        return money_flow

    def get_statistics(self) -> str:
        """
        Returns generated statistic about restaurant operations
        in string representation
        """
        order_count = len(self.hall_dispatcher.orders_list)
        total_money_flow = self.__total_money_flow
        current_date = dt.datetime.now()
        done_order_count = self.hall_dispatcher.done_orders_count()
        service_rate = self.hall_dispatcher.get_service_rate()

        return f"Orders created: {order_count}\n" \
               f"Done orders: {done_order_count}\n" \
               f"total money flow: {total_money_flow}\n" \
               f"Current time is {current_date}\n" \
               f"Service rate is {service_rate}\n"

    def get_transactions_history(self, period: PeriodBoundaries) -> \
            TransactionHistory:
        """
        Returns list of timestamp and total bill charged
        :param period: Tuple of 2 timestamps that bound some time period
        """
        transactions = list()

        left_bound = period[0]
        right_bound = period[1]

        for order in self.hall_dispatcher.orders_list:
            if left_bound < order.order_time < right_bound:
                transactions.append((order.order_id, order.price))

        return transactions
