"""Module contains human-like classes implementation"""
import datetime
import uuid
from random import random

from cookbook import cookbook
from restaurant import Problem, Storage


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

    def check_expired_food(self, storage: Storage) -> None:
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

    def solve_order_problem(self, problem: Problem) -> bool:
        """
        Solve given problem if possible
        :param problem: Problem to be solved
        :return: Return whether problem was solved
        """

    def get_customer_service_rate(self) -> int:
        """
        Give service rate about restaurant based on some metric
        :return: Return rate from range 0 to 5
        """


class Cook(Worker):
    """
    Represents cook of a restaurant
    """
    cookbook = cookbook

    def __init__(self, *args):
        super().__init__(*args)

        self.current_meal = ""
        self.estimation_time = None

    def start_cooking(self, meal: str) -> None:
        """
        Set estimation time and request goods that are needed
        :param meal: Name of a meal to be cooked
        :return: None
        """


class Customer:
    """
    Represents customer of a restaurant
    """

    def __init__(self, name=None, surname=None):
        self.customer_id = uuid.uuid4()
        self.name = name
        self.surname = surname

    def make_order(self) -> None:
        """
        Make some random order with some items from the menu
        :return:
        """

    def make_compliance(self, reason: str) -> Problem:
        """
        Makes compliance with some reason in it
        :param reason: String
        :return: New created problem
        """

    def leave(self) -> None:
        """Make customer to leave the restaurant"""
