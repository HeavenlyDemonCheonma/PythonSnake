import random

class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, grid):
        grid.drawSquare(screen, self.x, self.y, "Red")

    def randomisePosition(self, game):
        gridMaxX = game.grid.width - 1
        gridMaxY = game.grid.height - 1
        randomXY = (random.randint(0, gridMaxX), random.randint(0, gridMaxY))
        while randomXY in game.snake.snake or randomXY in game.apples.apples or randomXY in game.walls.walls:
            randomXY = (random.randint(0, gridMaxX), random.randint(0, gridMaxY))
        self.x, self.y = randomXY

    def getXY(self):
        return (self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, tuple):  # allow tuple comparison
            return (self.x, self.y) == other
        if isinstance(other, Apple):  # allow apple-to-apple comparison
            return (self.x, self.y) == (other.x, other.y)
        return False
