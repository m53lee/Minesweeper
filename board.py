from cell import Cell
import random


class Board:
    """
    Represents the board of the game.

    """

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.mines_num = self.set_mines_num(board_size)
        self.create_board()
        self.opened_cells = set()  # keeps track of opened cells as a tuple in a set
        self.win = False
        self.lose = False

    def getBoardSize(self):
        return self.board_size

    def getCell(self, row, col):
        return self.board[row][col]

    def set_mines_num(self, board_size):
        """
        Sets the number of mines on the board, which depends on the difficulty level chosen by the player.
        Beginner Level (9x9 board) = 10 mines
        Intermediate Level (16x16 board) = 40 mines
        """
        if board_size == 9:
            return 10
        if board_size == 16:
            return 40

    def create_board(self):
        """
        Board initialization.
        Place the mines randomly across the board.
        """
        mines_placed = 0

        # create new cell objects containing mines randomly on the board
        while mines_placed < self.mines_num:
            placement = random.randint(0, self.board_size ** 2 - 1)
            row = placement // self.board_size
            col = placement % self.board_size

            if self.board[row][col] is None:
                cell = Cell(1)
                self.board[row][col] = cell
                mines_placed += 1
        # create new cell objects for the remaining cells
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] is None:
                    cell = Cell(0)
                    self.board[row][col] = cell

        # set the numAround for all cells
        self.place_integers()

    def place_integers(self):
        """
        Sets the numAround attribute in all cells without a mine.
        """
        for row in range(self.board_size):
            for col in range(self.board_size):
                cell = self.board[row][col]
                if cell.getHasMine() == 0:
                    cell.setNumAround(self.count_integer(row, col))

    def count_integer(self, row, col):
        """
        Returns the number of mines surrounding a cell given in the parameter.
        """
        mines_count = 0
        # inspect adjacent cells to see how many mines are around
        for i in range(max(0, row - 1), min(self.board_size - 1, row + 1) + 1):
            for j in range(max(0, col - 1), min(self.board_size - 1, col + 1) + 1):
                cell = self.board[i][j]
                if cell.getHasMine() == 1:
                    mines_count += 1
        return mines_count

    def handleClick(self, index, cell, flag):
        # cell has already been clicked or flagged (left click on these cells are invalid)
        if cell.getClicked() or (cell.getFlagged() and not flag):
            return

        # cell has already been flagged, un-flag the cell
        if flag:
            cell.toggleFlag()
            return

        # first valid click of the game
        # if len(self.opened_cells) == 0:
        #     self.handleFirstClick(index)
        cell.setClickStatus()
        self.opened_cells.add(index)

        if cell.getNumAround() == 0:
            row, col = index[0], index[1]
            for i in range(max(0, row - 1), min(self.board_size - 1, row + 1) + 1):
                for j in range(max(0, col - 1), min(self.board_size - 1, col + 1) + 1):
                    if (i, j) not in self.opened_cells:
                        self.handleClick((i, j), self.board[i][j], False)

        if cell.getHasMine() == 1:
            self.lose = True

        else:
            self.win = self.checkWin()

    def checkWin(self):
        """
        Checks if there is a win in the game.
        """
        if len(self.opened_cells) == (self.board_size ** 2 - self.mines_num):
            return True
        return False

    def getWin(self):
        return self.win

    def getLose(self):
        return self.lose
