"""Module for string formatting"""


def format_str():
    """simple string C-style formatting"""

    data = ("John", "Doe", 53.44)
    format_string = "Hello %s %s. Your current balance is $%s."

    print(format_string % data)


if __name__ == "__main__":
    format_str()
