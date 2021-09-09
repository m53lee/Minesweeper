from game import Game
from board import Board


def main():
    board = Board(9)
    screenSize = (800, 800)
    game = Game(board, screenSize)
    game.run()


if __name__ == '__main__':
    main()
