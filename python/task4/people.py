"""Module contains human-like classes implementation"""
import datetime
import uuid
from random import random, choice

from cookbook import cookbook
from menu import menu
import orders
import restaurant


class Worker:
    """Implements functionality for worker of a restaurant"""

    def __init__(self, name: str, surname: str, passport: int):
        """
        :param name: Name of a worker
        :param surname: Surname of a worker
        :param passport: Passport of a worker
        """
        self.worker_id = uuid.uuid4()
        self.name = name
        self.surname = surname
        self._passport = passport
        self._job = None

    def set_job(self, job: str) -> bool:
        """
        Assign some job to be done by this worker
        :param job: Job to be done by this worker
        :return: Is job assigned
        :rtype: bool
        """
        if random() < 0.95:
            self._job = job
            return True
        print(f"Something went wrong. "
              f"{job} wasn't assigned to a {self.worker_id} worker")
        return False

    def check_expired_food(self, storage) -> None:
        """
        Start looking for expired goods in food storage
        :return: None
        """
        storage.write_off_food()
        print(f"Worker {self.worker_id} checked for expired goods "
              f"at {datetime.datetime.now()}")


class Manager(Worker):
    """Implements manager working functionality"""

    def __init__(self, *args):
        super().__init__(*args)

        self.current_state = None

    @staticmethod
    def promote_manager(worker_id: uuid) -> None:
        """
        Give a promotion to a worker
        :param worker_id: worker ID
        :return: None
        """

    def solve_order_problem(self, problem) -> bool:
        """
        Solve given problem if possible
        :param problem: Problem to be solved
        :return: Return whether problem was solved
        """
        problem.solve_problem()
        print(f"Problem {problem.problem_id} was solved by {self.worker_id}")
        return True

    def get_customer_service_rate(self) -> int:
        """
        Give service rate about restaurant based on some metric
        :return: Return rate from range 0 to 5
        """
        service_rate = int(random() * 5 + 1)
        print(f"{self.name} marked restaurant with {service_rate} starts")
        return service_rate


class Cook(Worker):
    """
    Represents cook of a restaurant
    """
    cookbook = cookbook

    def __init__(self, *args):
        super().__init__(*args)

        self._current_meal = None
        self.estimation_time = None

    @property
    def current_meal(self):
        """
        Property value of cook's current meal
        :return: Current meal of cook
        :rtype: str
        """
        return self._current_meal

    @current_meal.setter
    def current_meal(self, value: str):
        if value not in cookbook.keys():
            raise ValueError(f"Given meal doesn't in the menu: {value}")

        self._current_meal = value

    def start_cooking(self, meal: str) -> None:
        """
        Set estimation time and request goods that are needed
        :param meal: Name of a meal to be cooked
        :return: None
        """
        self.current_meal = meal
        self.estimation_time = cookbook[meal]


class Customer:
    """
    Represents customer of a restaurant
    """

    def __init__(self, name=None, surname=None):
        self.customer_id = uuid.uuid4()
        self.name = name
        self.surname = surname

    def make_order(self) -> orders.Order:
        """
        Make some random order with some items from the menu
        :return: Created order
        """
        selected_item = choice(sorted(menu.keys()))

        order = orders.Order(selected_item, self.customer_id)

        return order

    def make_compliance(self, reason: str) -> "restaurant.Problem":
        """
        Makes compliance with some reason in it
        :param reason: String
        :return: New created problem
        """

        return restaurant.Problem("problem", reason)

    def leave(self) -> None:
        """Make customer to leave the restaurant"""
        print(
            f"Customer {self.name}, id: {self.customer_id} "
            f"has left the restaurant")
