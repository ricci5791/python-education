"""Module contains game logic and render classes"""
import csv
import random as rnd

from frames import char_frames


class Game:
    """Class which contains info about current game"""

    class Render:
        """Contains methods required to output the game state to a user"""
        char_field = char_frames

        def __init__(self):
            self.__frame_counter = 0
            self.__word = None
            self.word_mask = None

        def __print_frame(self) -> None:
            """Prints guillotine from prepared file"""
            print(self.char_field[self.__frame_counter])

        def __print_game_info(self,
                              avail_attempts: int,
                              letters_list: list[str]) -> None:
            """
            Shows info about game word, attempts left
            and list of used letters
            """
            print(f"Current word: {self.word_mask}\n"
                  f"Was used next letters: {letters_list}\n"
                  f"{avail_attempts} attempts left.")

        def start_render_cycle(self, cycle_type: str,
                               avail_attempts: int,
                               letters_list: list[str]) -> None:
            """
            Accept predefined state and operates in order to show
            guillotine, letters and other game info
            :param cycle_type: Snake_typing string describes a case of call
            :param avail_attempts: Count of available attempts
            :param letters_list: List of letters that was used previously
            """

            if cycle_type == "wrong_letter":
                self.__frame_counter += 1
            elif cycle_type == "end_game":
                self.__frame_counter += 1
                print("You have used all your attempts! Try new game :)")
                print(f"The word was {self.__word}\n")
            elif cycle_type == "win_game":
                print("Congratulation to you. Victory is yours!")

            self.__print_frame()
            self.__print_game_info(avail_attempts, letters_list)

        def set_word(self, word: str) -> None:
            """
            Set given word and created mask based on this word to a renderer
            :param word: A word to be set
            """
            self.__word = word
            self.word_mask = ["_" for _ in range(len(word))]

        def set_letter(self, index: int, letter: str) -> None:
            """
            Reveal letter at specific index
            :param index: Index of a letter to be revealed
            :param letter: A letter to be revealed
            """
            self.word_mask[index] = letter

    def __init__(self):
        self.__state = 0
        self.avail_attempts = 6
        self.used_letters = list()
        self.renderer = Game.Render()
        self.__word = None
        self.__word_mask = 1
        self.__win_game_mask = None

    def start_game(self) -> None:
        """Starts a game session with word with specified length"""
        if self.__word is None:
            self.__read_words_file()

        self.renderer.set_word(self.__word)

        self.__set_masks()
        self.__take_input()

    def set_custom_word(self) -> None:
        """Sets custom word to be solved. Should be less than 25 characters"""
        custom_word = input("Type desired word (should contain letters only)")

        while not custom_word.isalpha() or \
                len(custom_word) > 25 or \
                self.__is_exit_word(custom_word):
            custom_word = input("Wrong input! "
                                "Try again(word should contain letters only) "
                                "or exit")

        self.__word = custom_word

    def __read_words_file(self) -> None:
        """Reads words from words_list.csv"""
        with open('words_list.csv') as file:
            reader = list(csv.reader(file))
            self.__word = str(reader[rnd.randint(0, len(reader) - 1)][0])

    def __set_masks(self) -> None:
        """Sets word bit mask to the size of mask_size"""
        mask_size = len(self.__word)

        self.__word_mask = 1 << mask_size
        self.__win_game_mask = (1 << mask_size + 1) - 1

    def __is_exit_word(self, word: str) -> bool:
        """Checks whether given word is 'esc'"""
        return word.lower() == "esc"

    def __search_letter(self, user_letter: str) -> int:
        """
        Searches for a given letter in the word
        :param user_letter: Letter to be searched
        :return: bool
        """
        for index, letter in enumerate(self.__word):
            if letter == user_letter and not self.__word_mask & (1 << index):
                self.__word_mask |= (1 << index)
                return index + 1
        return 0

    def __take_input(self):
        """
        Contains infinite loop. Takes input from user until
        either end attempts or word is solved.
        The game can be interrupted with 'ESC' word
        """
        is_end = False

        self.renderer.start_render_cycle("correct_letter",
                                         self.avail_attempts,
                                         self.used_letters)

        while not is_end:
            user_input = input("Enter a letter\n")
            if self.__is_exit_word(user_input):
                break

            self.used_letters.append(user_input)

            search_index = self.__search_letter(user_input)
            state = "correct_letter"

            if not search_index:
                self.avail_attempts -= 1
                state = "wrong_letter"
            else:
                self.renderer.set_letter(search_index - 1, user_input)

            if self.avail_attempts == 0:
                state = "end_game"
                is_end = True

            if self.__word_mask == self.__win_game_mask:
                state = "win_game"
                is_end = True

            self.renderer.start_render_cycle(state,
                                             self.avail_attempts,
                                             self.used_letters)
