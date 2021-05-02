"""Module with funtions that accept multiple parameter list
and keywords parameters"""


class MultiFunctions:
    """class that contains functions which can
    accept from changeable list of parameters both positional and keywords"""

    def foo(self, a, b, c, *args):
        """accept at least 3 positional parameters and return its length"""

        return len(list(args))

    def bar(self, a, b, c, **kwargs):
        """accept keywords parameters
        and return boolean whether 'magicnumber' is 7"""

        return kwargs.get("magicnumber") == 7

    def perform_test(self):
        """evaluate how present functions work"""

        if self.foo(1, 2, 3, 4) == 1:
            print("Good.")
        if self.foo(1, 2, 3, 4, 5) == 2:
            print("Better.")
        if not self.bar(1, 2, 3, magicnumber=6):
            print("Great.")
        if self.bar(1, 2, 3, magicnumber=7):
            print("Awesome!")


if __name__ == "__main__":
    multi_func = MultiFunctions()
    multi_func.perform_test()
