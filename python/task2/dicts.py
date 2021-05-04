"""Module with basic dict add/remove actions"""


class Phonebook:
    """Class that use add/remove actions with dict"""

    def __init__(self):
        self.phonebook = {"John": 938477566, "Jack": 938377264,
                          "Jill": 947662781}

    def change_dict(self):
        """Work with dict - delete 'Jill' keypair
        and add 'Jake' key with some data"""
        self.phonebook["Jake"] = 938273443
        self.phonebook.pop("Jill")

    def test(self):
        """perform some tests after changes are done"""
        if "Jake" in self.phonebook:
            print("Jake is listed in the phonebook.")

        if "Jill" not in self.phonebook:
            print("Jill is not listed in the phonebook.")


if __name__ == "__main__":
    phonebook = Phonebook()

    phonebook.change_dict()
    phonebook.test()
