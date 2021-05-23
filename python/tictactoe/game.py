"""Module with game logic"""
from typing import Tuple

from render import Render


class TicTacToe:
    """Implements tic-tac-toe game logic"""

    def __init__(self):
        self.game_field = [str(i + 1) for i in range(9)]
        self.moves = list()
        self.first_player, self.second_player = None, None
        self.curr_player_mark = "O"
        self.render = Render()

    def make_move(self, move: int) -> bool:
        """
        Takes where to place player's mark and does it if possible

        :param move: Where to place (starts from 1 to 9)
        :return: True if move is made, False otherwise
        :rtype: bool
        """
        move -= 1

        if self.game_field[move] == str(move + 1):
            self.game_field[move] = self.curr_player_mark
            self.moves.append((self.curr_player_mark, move))
            return True

        return False

    def is_winning(self, player_mark: str) -> bool:
        """
        Checks if given player won the game

        :param player_mark: Current player's mark
        :return: True if player won the game, False otherwise
        :rtype: bool
        """
        if len(self.moves) < 4:
            return False

        field = [self.game_field[i] == player_mark for i in range(9)]

        for i in range(3):
            if all(field[i * 3: i * 3 + 3]) or all(field[i::3]):
                return True

        if all(field[::4]) or all(field[2:7:2]):
            return True

        return False

    def set_players_names(self, player_names: Tuple[str, str]) -> None:
        """
        Save players names to a game state

        :param player_names: Tuple[str, str]
        :return: None
        """
        self.first_player, self.second_player = player_names

    def change_curr_player(self):
        """
        Change current player mark to the opposite one

        :return: None
        """
        if self.curr_player_mark == "X":
            self.curr_player_mark = "O"
        else:
            self.curr_player_mark = "X"

    def get_curr_player_name(self) -> str:
        """
        Return current player's name

        :return: Name of the player
        :rtype: str
        """
        return self.first_player if self.curr_player_mark == "O" \
            else self.second_player

    def start_game_cycle(self) -> None:
        """
        Starts game cycle and operates with the game state

        :return: None
        """
        self.set_players_names(self.render.get_names())

        while True:
            self.render.show_field(self.game_field)
            user_move = self.render.get_player_move(self.get_curr_player_name())

            if not self.make_move(user_move):
                self.render.show("Something went wrong! Try again")
                continue

            if self.is_winning(self.curr_player_mark):
                self.render.show(f"Congratulation "
                                 f"{self.get_curr_player_name()}, you won!")
                break

            self.change_curr_player()
