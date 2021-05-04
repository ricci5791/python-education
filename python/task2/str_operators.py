"""Module with """


def str_operators():
    """shows basic str operators in python3"""

    string = "Strings are awesome!"
    # Length should be 20
    print("Length of s = %d" % len(string))

    # First occurrence of "a" should be at index 8
    print("The first occurrence of the letter a = %d" % string.index("a"))

    # Number of a's should be 2
    print("a occurs %d times" % string.count("a"))

    # Slicing the string into bits
    print("The first five characters are '%s'" % string[:5])
    print("The next five characters are '%s'" % string[5:10])
    print("The thirteenth character is '%s'" % string[12])
    print("The characters with odd index are '%s'" % string[1::2])
    print("The last five characters are '%s'" % string[-5:])

    # Convert everything to uppercase
    print("String in uppercase: %s" % string.upper())

    # Convert everything to lowercase
    print("String in lowercase: %s" % string.lower())

    # Check how a string starts
    if string.startswith("Str"):
        print("String starts with 'Str'. Good!")

    # Check how a string ends
    if string.endswith("ome!"):
        print("String ends with 'ome!'. Good!")

    # Split the string into three separate strings,
    # each containing only a word
    print("Split the words of the string: %s" % string.split(" "))


if __name__ == "__main__":
    str_operators()
