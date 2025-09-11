import Wall

class WallList:
    walls = []
    def __init__(self):
        self.walls = []

    def draw(self, game):
        for wall in self.walls:
            wall.draw(game)

    def addWall(self, *toupleXY):
        for wallXY in toupleXY:
            self.walls.append(Wall.Wall(wallXY[0], wallXY[1]))