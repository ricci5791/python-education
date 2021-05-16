"""Module contains human-like classes implementation"""
import uuid

from cookbook import cookbook


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
        """

    def check_expired_food(self) -> None:
        """
        Start looking for expired goods in food storage
        :return: None
        """


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

    def solve_order_problem(self, problem_id: uuid) -> bool:
        """
        Solve given problem if possible
        :param problem_id:
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
