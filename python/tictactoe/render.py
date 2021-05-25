"""Module with render-associated classes: Render and Tkinter"""
from typing import List, Tuple

import os
import re
import prettytable


class Render:
    """
    Render class that can show tic-tac-toe field
    """

    def __init__(self):
        self.text_table = prettytable.PrettyTable()
        self.text_table.header = False
        self.text_table.hrules = prettytable.ALL

    @staticmethod
    def show(string: str) -> None:
        """
        Prints some given info

        :param string: Info to print
        :return: None
        """
        print(string)

    def show_field(self, game_field: List[str]):
        """
        Clear console and prints given list of chars as square game field

        :param game_field: List of chars
        :type game_field: List[str]
        :return: None
        """
        self.text_table.clear()

        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        rows_slices = [game_field[:3], game_field[3: 6], game_field[6:]]

        self.text_table.add_rows(rows_slices)

        print(self.text_table)

    @staticmethod
    def get_names() -> Tuple[str, str]:
        """
        Gets names of current players as input and return it

        :return: Tuple[str]
        """
        print("Remember! Only latin chars allowed")

        first_player_name = input("Enter first player name: \n")
        second_player_name = input("Enter second player name: \n")

        while re.findall(r"[^A-z\s]", first_player_name + second_player_name) \
                or first_player_name == second_player_name:
            print("Wrong names! Try again. \n")

            first_player_name = input("Enter first player name: \n")
            second_player_name = input("Enter second player name: \n")

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
            user_input = int(input(f"{player_name} make your step: "))

        return user_input

    @staticmethod
    def show_menu() -> int:
        """
        Takes user input from 1 to 5 as menu points

        :return:  Chosen point from the menu
        :rtype: int
        """
        print("1: new game")
        print("2: replay game")
        print("3: show logs")
        print("4: delete logs")
        print("5: exit")

        user_input = input("Choose point from the menu below: ")

        while re.findall(r"\D", user_input) or not 0 < int(user_input) < 6:
            print("Incorrect input! Try again, only digits are allowed")
            user_input = input("Choose point from the menu: ")

        return int(user_input)
