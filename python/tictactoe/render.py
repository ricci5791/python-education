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

        if re.findall(r"\W", first_player_name + " " + second_player_name) and \
                first_player_name != second_player_name:
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
