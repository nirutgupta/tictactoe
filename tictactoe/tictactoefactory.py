from tictactoe.board import TicTacToeBoard
from tictactoe.player import HumanPlayer
from tictactoe.tictactoe_board_symbol import TicTacToeBoardSymbol
from tictactoe.tictactoegame import TicTacToeGame


class TicTacToeFactory:

    @staticmethod
    def get_standard_3x3_game():
        p1 = HumanPlayer("Nirut")
        p2 = HumanPlayer("Interviewer")
        board = TicTacToeBoard(3, 3)

        return TicTacToeGame(board, [p1, p2], [TicTacToeBoardSymbol.X, TicTacToeBoardSymbol.O])
