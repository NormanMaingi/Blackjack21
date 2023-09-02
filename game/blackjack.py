# Imports
import sys
from random import choice
import player
import cards
import game_engine as gm


def main():
    # Start the Game
    game = gm.Game(1)
    game.menu()


# Main function call#
if __name__ == "__main__":
    main()
