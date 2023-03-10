from tictactoe.tictactoe_board_symbol import TicTacToeBoardSymbol


class TicTacToeBoard:

    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = [[TicTacToeBoardSymbol.E for i in range(num_cols)] for j in range(num_rows)]

    def is_full(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.board[row][col] == TicTacToeBoardSymbol.E:
                    return False
        return True

    def has_captured_row(self, symbol):
        for row in range(self.num_rows):
            is_row_captured = True
            for col in range(self.num_cols):
                if self.board[row][col] != symbol:
                    # print(f"i am here {symbol}")
                    is_row_captured = False
            if is_row_captured:
                return True
        return False

    def has_captured_column(self, symbol):
        for col in range(self.num_cols):
            is_col_captured = True
            for row in range(self.num_rows):
                if self.board[row][col] != symbol:
                    # print(f"i am here {symbol}")
                    is_col_captured = False
            if is_col_captured:
                return True
        return False

    def has_captured_diagonal(self, symbol):
        # TODO implement
        return False

    def display(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(f"| {self.board[row][col].value}", end=" ")
            print("|")

    def set(self, row, col, value: TicTacToeBoardSymbol):
        # validate if already filled
        self.board[row][col] = value

