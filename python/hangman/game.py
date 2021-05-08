"""Module contains game logic and render classes"""
import csv
import random as rnd


class Game:
    """Class which contains info about current game"""

    class Render:
        """Contains methods required to output the game state to a user"""

    def __init__(self):
        self.__state = 0
        self._avail_attempts = 5
        self.used_letters = list()
        self.renderer = Game.Render()
        self.word = None

    def start_game(self) -> None:
        """Starts a game session with word with specified length"""
        if self.word is None:
            self.__read_words_file()
        self.__take_input()

    def set_custom_word(self) -> None:
        """Sets custom word to """
        custom_word = input("Type desired word (should contain letters only)")

        while not custom_word.isalpha() or custom_word.lower() == "esc":
            custom_word = input("Wrong input! "
                                "Try again(word should contain letters only) "
                                "or exit")

        self.word = custom_word

    def __read_words_file(self):
        """Reads words from words_list.csv"""
        with open('words_list.csv') as file:
            reader = list(csv.reader(file))
            self.word = reader[rnd.randint(0, len(reader))]

    def __take_input(self):
        """
        Contains infinite loop. Takes input from user until
        either end attempts or word is solved.
        The game can be interrupted with 'ESC' word
        """
        while True:
            user_input = input()
