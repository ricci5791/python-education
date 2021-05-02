"""Module with list comprehension class in it"""


class BasicOperators:
    """class which shows list comprehension usage"""

    def __init__(self):
        """__init__ function with setting up properties"""
        self.x_item = object()
        self.y_item = object()
        self.x_list = list()
        self.y_list = list()
        self.big_list = list()

    def transform_lists(self):
        """transforms class properties with list comprehension"""
        self.x_list = [self.x_item] * 10
        self.y_list = [self.y_item] * 10
        self.big_list = self.x_list + self.y_list

    def check_result(self):
        """print out result of class work"""
        print("x_list contains %d objects" % len(self.x_list))
        print("y_list contains %d objects" % len(self.y_list))
        print("big_list contains %d objects" % len(self.big_list))

        if self.x_list.count(self.x_item) == 10 \
                and self.y_list.count(self.y_item) == 10:
            print("Almost there...")
        if self.big_list.count(self.x_item) == 10 \
                and self.big_list.count(self.y_item) == 10:
            print("Great!")


if __name__ == "__main__":
    operators = BasicOperators()
    operators.transform_lists()
    operators.check_result()
