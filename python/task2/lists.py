"""Module with list appender function"""


def lists_appender():
    """List appender for numbers, strings.
    Also extract element with bracket operator"""

    nums = []
    words = []
    names = ["John", "Eric", "Jessica"]

    second_word = names[1]

    for i in range(1, 4):
        nums.append(i)

    words.append("hello")
    words.append("world")

    return nums, words, second_word


if __name__ == "__main__":
    numbers, strings, second_name = lists_appender()

    print(numbers)
    print(strings)
    print("The second name on the names list is %s" % second_name)
