import enum

class Direction(enum.Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


    def getOpposite(self):
        if self.value == Direction.UP:
            return Direction.DOWN
        elif self.value == Direction.DOWN:
            return Direction.UP
        elif self.value == Direction.LEFT:
            return Direction.RIGHT
        elif self.value == Direction.RIGHT:
            return Direction.LEFT
