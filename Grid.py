import Square as Square
import pygame

class Grid:
    def __init__(self, width, height, squareSize, color1, color2, y_offset = 0, x_offset = 0):
        squareArray = [] #Create empty list
        for i in range(width):
            squareArray.append([]) #Append empty list to squareArray
            for j in range(height):
                #Create square and append it to list
                square = Square.Square(squareSize, color1 if (i + j) % 2 == 0 else color2) #Create square
                squareArray[i].append(square) #Append square to list

        self.grid = squareArray
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.width = width
        self.height = height


    def drawWholeGrid(self, screen):
        for rowIndex, row in enumerate(self.grid):
            for colIndex, square in enumerate(row):
                pygame.draw.rect(screen, square.color,
                                 (square.size * rowIndex + self.x_offset, square.size * colIndex + self.y_offset,
                                  square.size, square.size))


    def drawSquare(self, screen, x, y, color):
        pygame.draw.rect(screen, color,
                         (self.grid[x][y].size * x + self.x_offset, self.grid[x][y].size * y + self.y_offset,
                          self.grid[x][y].size, self.grid[x][y].size))


