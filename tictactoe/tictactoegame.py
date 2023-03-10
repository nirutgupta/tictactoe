from typing import List

from tictactoe.move import Move
from tictactoe.player import Player
from tictactoe.tictactoe_board_symbol import TicTacToeBoardSymbol
from tictactoe.board import TicTacToeBoard
from tictactoe.igame import IGame


class TicTacToeGame(IGame):
    """
    Tic-Tac-Toe Game implements IGame
    """

    def __init__(self, board: TicTacToeBoard, players: List[Player], symbols: List[TicTacToeBoardSymbol]):
        self.board_state = board
        self.players = players
        self.current_player_index = 0
        self.symbols = symbols

    def has_winner(self):
        symbol = self.symbols[self.current_player_index]
        return self.board_state.has_captured_row(symbol) or self.board_state.has_captured_column(
            symbol) or self.board_state.has_captured_diagonal(symbol)

    def get_game_winner(self):
        return self.get_current_player().name

    def is_draw(self):
        return self.board_state.is_full()

    def display_board_state(self):
        self.board_state.display()

    def get_current_player(self):
        return self.players[self.current_player_index]

    def make_move(self):
        current_player: Player = self.get_current_player()
        move: Move = current_player.make_move(self.board_state)
        self.board_state.set(move.row, move.col, self.symbols[self.current_player_index])

    def update_current_player(self):
        print("updating current player")
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def get_board_state(self):
        return self.board_state
