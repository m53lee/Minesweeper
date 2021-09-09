class Cell:
    """
    Represents each cell on the board.
    Attributes include:
    - does the cell contain a mine?
    - how many mines are surrounding the cell if the cell does not contain a mine?
    - Clicked?
    - Flagged?
    - The neighbors that represent the surrounding cells.
    """

    def __init__(self, hasMine):
        self.hasMine = hasMine
        self.numAround = 0
        self.clicked = False
        self.flagged = False
        self.neighbors = []

    def getHasMine(self):
        """ returns True if the cell contains a mine, if not return False """
        return self.hasMine

    def setNumAround(self, num):
        """
        If the cell is not a mine, then there should be a number in the cell that represents the number of mines
        surrounding the cell.
        """
        self.numAround = num

    def getNumAround(self):
        """ get the number of mines around the cell """
        return self.numAround

    def setClickStatus(self):
        """ sets the clicked status to True """
        self.clicked = True

    def getClicked(self):
        """ returns True if the cell was clicked, if not return False """
        return self.clicked

    def getFlagged(self):
        """ returns True if the cell was flagged, if not return False """
        return self.flagged

    def toggleFlag(self):
        """ unflag the flagged cell """
        self.flagged = not self.flagged

    def setNeighbors(self, neighbors):
        """ sets the neighbors array """
        self.neighbors = neighbors

    def getNeighbors(self):
        """ gets the neighbors array """
        return self.neighbors
