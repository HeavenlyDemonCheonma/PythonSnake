import Apple

class AppleList:
    apples = []
    def __init__(self):
        self.apples = []

    def addApple(self, game, count = 1):
        for apple in range(count):
            apple = Apple.Apple(0, 0)
            apple.randomisePosition(game)
            self.apples.append(apple)

    def removeApple(self, x, y):
        for apple in self.apples:
            if apple.x == x and apple.y == y:
                self.apples.remove(apple)
                break

    def eatApple(self, x, y, game):
        for apple in self.apples:
            if apple.x == x and apple.y == y:
                self.apples.remove(apple)
                self.addApple(game)
                break


    def draw(self, screen, grid):
        for apple in self.apples:
            apple.draw(screen, grid)

    def getXYList(self):
        return [(apple.x, apple.y) for apple in self.apples]

    def getApple(self, position):
        for apple in self.apples:
            if apple.getXY() == position:
                return apple
