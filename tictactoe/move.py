from abc import ABC, abstractmethod


class Move(ABC):
    @property
    @abstractmethod
    def row(self):
        pass

    @property
    @abstractmethod
    def col(self):
        pass


class TicTacToeMove(Move):
    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    def __init__(self, row, col):
        self._row = row
        self._col = col
