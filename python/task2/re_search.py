"""Module that searches some word in names of given module functions"""
import re


def search_word(word="find"):
    """Search for some specific name in 're' module functions"""

    match_list = list()

    regex = re.compile(word)

    for item in dir(re):
        if regex.match(item):
            match_list.append(item)

    print(match_list)


if __name__ == "__main__":
    search_word()
