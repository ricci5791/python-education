"""Module with a class which shows difference between 2 sets"""


class SetDiff:
    """Can show difference between 2 sets"""

    def __init__(self):
        self.a_set = {"Jake", "John", "Eric"}
        self.b_set = {"John", "Jill"}

    def print_diff(self):
        """Print out difference between 2 sets"""
        print(self.a_set.difference(self.b_set))


if __name__ == "__main__":
    set_diff = SetDiff()
    set_diff.print_diff()
