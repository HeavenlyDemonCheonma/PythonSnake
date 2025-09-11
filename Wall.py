class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def draw(self, game):
        game.grid.drawSquare(game.screen, self.x, self.y, "DarkGrey")

    def __eq__(self, other):
        if isinstance(other, tuple):  # allow tuple comparison
            return (self.x, self.y) == other
        if isinstance(other, Wall):  # allow apple-to-apple comparison
            return (self.x, self.y) == (other.x, other.y)
        return False