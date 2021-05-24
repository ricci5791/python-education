"""Module with render-associated classes: Render and Tkinter"""
import re
from typing import List, Tuple


class Render:
    """
    Render class that can show tic-tac-toe field
    """

    @staticmethod
    def show(string: str) -> None:
        """
        Prints some given info

        :param string: Info to print
        :return: None
        """
        print(string)

    @staticmethod
    def show_field(game_field: List[str]):
        """
        Prints given list of chars as square game field

        :param game_field: List of chars
        :type game_field: List[str]
        :return: None
        """
        rows_slices = [game_field[:3], game_field[3: 6], game_field[6:]]
        for row in rows_slices:
            print(row)

    @staticmethod
    def get_names() -> Tuple[str, str]:
        """
        Gets names of current players as input and return it

        :return: Tuple[str]
        """
        print("Remember! Only latin chars allowed")

        first_player_name = input("Enter first player name")
        second_player_name = input("Enter second player name")

        while re.findall(r"[^A-z\s]", first_player_name + second_player_name) \
                or first_player_name == second_player_name:
            print("Wrong names! Try again. \n")

            first_player_name = input("Enter first player name")
            second_player_name = input("Enter second player name")

        return first_player_name, second_player_name

    @staticmethod
    def get_player_move(player_name: str) -> int:
        """
        Takes player name and return move that the player intends to do

        :param player_name: Player name to display
        :return: Position of char to be placed by this player
        :rtype: int
        """
        user_input = -1

        while not 0 < user_input < 10:
            print("Choose cell from 1 to 9")
            user_input = int(input(f"{player_name} make your step"))

        return user_input

    def show_menu(self) -> int:
        """
        Takes user input from 1 to 3 as menu points

        :return:  Chosen point from the menu
        :rtype: int
        """
        print("1: new game")
        print("2: replay game")
        print("3: show logs")

        user_input = input("Choose point from the menu below:")

        while re.findall(r"\D", user_input) or not (0 < int(user_input) < 4):
            print("Incorrect input! Try again, only digits are allowed")
            user_input = input("Choose point from the menu:")

        return int(user_input)
