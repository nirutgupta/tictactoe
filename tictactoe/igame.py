from abc import ABC, abstractmethod


class IGame(ABC):
    """
    Template for a 2 player game
    """

    def play(self):
        print("Starting board game")
        while not self.has_winner() and not self.is_draw():
            self.update_current_player()
            # p: Player = self.get_current_player()
            print("Current game state")
            self.display_board_state()
            self.make_move()
        self.display_board_state()
        if self.is_draw():
            print("Game Drawn")
            return
        if self.has_winner():
            print(f"Winner is {self.get_game_winner()}")

    @abstractmethod
    def has_winner(self):
        pass

    @abstractmethod
    def is_draw(self):
        pass

    @abstractmethod
    def display_board_state(self):
        pass

    @abstractmethod
    def get_current_player(self):
        pass

    @abstractmethod
    def make_move(self):
        pass

    @abstractmethod
    def get_board_state(self):
        pass

    @abstractmethod
    def get_game_winner(self):
        pass

    @abstractmethod
    def update_current_player(self):
        pass
