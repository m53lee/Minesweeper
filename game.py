import os
import pygame


class Game:
    def __init__(self, board, screenSize):
        self.images = {}
        self.board = board
        self.screenSize = screenSize
        self.squareSize = self.screenSize[0] // self.board.getBoardSize(), self.screenSize[
            1] // self.board.getBoardSize()
        self.loadImages()
        self.screen = pygame.display.set_mode(self.screenSize)

    def run(self):
        pygame.init()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and (not self.board.getWin() or not self.board.getLose()):
                    rightClick = pygame.mouse.get_pressed(num_buttons=3)[2]
                    self.handleClick(pygame.mouse.get_pos(), rightClick)
            self.draw()
            pygame.display.flip()
            if self.board.getWin():
                running = False
        pygame.quit()

    def draw(self):
        topLeft = (0, 0)
        for row in range(self.board.getBoardSize()):
            for square in range(self.board.getBoardSize()):
                cell = self.board.getCell(row, square)
                image = self.images[self.getImage(cell)]
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.squareSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.squareSize[1]

    def loadImages(self):
        """
        Takes the images in the 'Images' folder and stores them in a dictionary.
        """
        for fileName in os.listdir("images"):
            if fileName.endswith(".png"):
                image = pygame.image.load(r"images/" + fileName)
                image = pygame.transform.scale(image, self.squareSize)
                self.images[fileName.split(".")[0]] = image

    def getImage(self, cell):
        if cell.getClicked():
            return "bomb-at-clicked-block" if cell.getHasMine() else str(cell.getNumAround())

        if self.board.getLose():
            if cell.getHasMine() == 1:
                return "bomb"
        return 'flag' if cell.getFlagged() else 'empty-block'

    def handleClick(self, pos, flag):
        index = pos[1] // self.squareSize[1], pos[0] // self.squareSize[0]
        cell = self.board.getCell(index[0], index[1])
        self.board.handleClick(index, cell, flag)
