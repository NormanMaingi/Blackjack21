import sys
import player as plyer


class Game:
    def __init__(self, game_id):
        self.game_id = game_id

    def menu(self):
        print("Welcome To BlackJack")
        start_game = int(input("Select \n1) Play \n2) Exit \n"))
        if start_game == 1:
            Game.engine(plyer)
        else:
            sys.exit()

    @staticmethod
    def engine(player):
        player = plyer.Player()
        player.player_info()

    def new_game(self):
        ...

    def compare_values(self):
        ...
