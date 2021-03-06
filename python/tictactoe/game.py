"""Module with game logic"""
import logging
from typing import Tuple

from render import Render


class TicTacToe:
    """Implements tic-tac-toe game logic"""

    MENU_NEW_GAME = 1
    MENU_REPLAY_GAME = 2
    MENU_SHOW_LOGS = 3
    MENU_CLEAR_LOGS = 4
    MENU_EXIT = 5

    def __init__(self, save_prev_names: bool = False):
        self.game_field = [str(i + 1) for i in range(9)]
        self.moves_count = 0
        if not save_prev_names:
            self.first_player, self.second_player = None, None
            self.victory_counter = [0, 0]
        self.curr_player_mark = "O"
        self.render = Render()

        logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s, %(levelname)s - %(message)s",
                            datefmt="%d-%b-%y %H:%M:%S",
                            filename="game_logs.log")

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
            self.moves_count += 1
            return True

        return False

    def is_winning(self, player_mark: str) -> bool:
        """
        Checks if given player won the game

        :param player_mark: Current player's mark
        :return: True if player won the game, False otherwise
        :rtype: bool
        """
        if self.moves_count < 4:
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

    def change_curr_player(self) -> None:
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

    def game_cycle(self) -> None:
        """
        Starts game with existing players

        :return: None
        """
        while True:
            self.render.show_field(self.game_field)
            user_move = self.render.get_player_move(self.get_curr_player_name())

            if not self.make_move(user_move):
                self.render.show("Something went wrong! Try again")
                continue

            if self.is_winning(self.curr_player_mark):
                if self.curr_player_mark == "O":
                    self.victory_counter[0] += 1
                else:
                    self.victory_counter[1] += 1

                logging.info(
                        "Player %s won; %s(%i vs %i)%s total moves made is %i",
                        self.get_curr_player_name(),
                        self.first_player,
                        self.victory_counter[0],
                        self.victory_counter[1],
                        self.second_player,
                        self.moves_count)
                self.render.show(f"Congratulation "
                                 f"{self.get_curr_player_name()}, you won!")
                break

            self.change_curr_player()

    def start_new_game_cycle(self) -> None:
        """
        Starts game cycle and operates with the game state

        :return: None
        """
        self.__init__()

        self.set_players_names(self.render.get_names())

        self.game_cycle()

    def start_game_cycle(self) -> None:
        """
        Continue playing with set players

        :return: None
        """
        self.__init__(True)

        if self.first_player is None and self.second_player is None:
            self.render.show("You haven't played any games")
            return

        self.game_cycle()

    def show_menu(self) -> None:
        """
        Control menu interaction with user

        :return: None
        """
        while True:
            menu_choice = self.render.show_menu()

            if menu_choice == self.MENU_NEW_GAME:
                self.start_new_game_cycle()
            elif menu_choice == self.MENU_REPLAY_GAME:
                self.start_game_cycle()
            elif menu_choice == self.MENU_SHOW_LOGS:
                with open("game_logs.log") as log_file:
                    print(log_file.read())
            elif menu_choice == self.MENU_EXIT:
                break
            elif menu_choice == self.MENU_CLEAR_LOGS:
                open("game_logs.log", "w").close()
                self.render.show("Logs was deleted!\n")
