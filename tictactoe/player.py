from abc import ABC, abstractmethod

from tictactoe.move import Move, TicTacToeMove


class Player(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def make_move(self, board_state):
        pass


class HumanPlayer(Player):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def make_move(self, board_state) -> Move:
        print("Player Visible State")
        print(board_state.display())
        print(f"{self._name} : Enter row,col")
        s = input()
        row, col = s.split(",")
        # create move of the input and return
        print("sending move")
        return TicTacToeMove(int(row), int(col))
