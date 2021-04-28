"""
This module provides basic calculator with adding, subtraction, division and
multiplying
"""


class Calculator:
    """Simple class which contain 4 method for basic math operations"""

    def __init__(self):
        self.operations_history = list()

    def add(self, first_num: int, second_num: int) -> int:
        """Provide add function which requires:
        2 integer parameters and returns sum of it"""
        result = first_num + second_num

        self.operations_history.append({"op": "+",
                                        "nums": (first_num, second_num),
                                        "res": result})

        return result

    def subtract(self, first_num: int, second_num: int) -> int:
        """Provide subtraction function which requires:
        2 integer parameters and returns integer sum of it"""
        result = first_num - second_num

        self.operations_history.append({"op": "-",
                                        "nums": (first_num, second_num),
                                        "res": result})

        return result

    def multiply(self, first_num: int, second_num: int) -> int:
        """Provide multiplying function which requires:
        2 integer parameters and returns integer multiplying of it"""
        result = first_num * second_num

        self.operations_history.append({"op": "*",
                                        "nums": (first_num, second_num),
                                        "res": result})

        return result

    def divide(self, first_num: int, second_num: int) -> float:
        """Provide division function which requires:
        2 integer parameters and returns float division of it"""
        result = first_num / second_num

        self.operations_history.append({"op": "/",
                                        "nums": (first_num, second_num),
                                        "res": result})

        return result
