from tictactoe.tictactoefactory import TicTacToeFactory
from tictactoe.tictactoegame import TicTacToeGame

game: TicTacToeGame = TicTacToeFactory.get_standard_3x3_game()
game.play()
