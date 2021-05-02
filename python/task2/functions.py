"""Module with function use """


def list_benefits():
    """create and return list of strings"""
    return ["More organized code", "More readable code", "Easier code reuse",
            "Allowing programmers to share and connect code together"]


def build_sentence(benefit):
    """Takes string argument 'benefit' and append to it the sentence"""
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    """Prints benefits of function use"""

    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


if __name__ == "__main__":
    name_the_benefits_of_functions()
