import Direction
import pygame
import itertools

class Snake:
    snake = []
    direction = Direction.Direction.RIGHT
    hasMovedAfterDirectionChange = False
    nextDirectionKey = None
    keyPresses = []

    def __init__(self, length):
        self.head = (5, 5)  # starting position
        self.snake = [self.head]  # snake body list
        self.length = length
        self.keyPresses = []

        self.hasMovedAfterDirectionChange = False

    def move(self, game):
        self.updateDirection()
        grid_width = game.grid.width
        grid_height = game.grid.height
        dx, dy = self.direction.value
        if game.border:
            # do not allow snake to go out of bounds
            # add direction values to head position
            new_head = self.head[0] + dx, self.head[1] + dy
        else:
            # allow snake to go out of bounds
            # use modulo to wrap around the screen
            new_head = ((self.head[0] + dx) % grid_width,
                        (self.head[1] + dy) % grid_height)
        outOfBounds = new_head[0] < 0 or new_head[0] >= grid_width or new_head[1] < 0 or new_head[1] >= grid_height


        if new_head in self.snake or new_head in game.walls.walls:
            # snake collides with itself
            print("Game over")
            game.quit()
            return
        elif game.border and outOfBounds:
            # snake collides with wall
            print("Game over")
            game.quit()
            return
        elif new_head in game.apples.getXYList():
            # snake eats apple
            game.apples.eatApple(new_head[0], new_head[1], game)
            game.score += 1
            self.snake.append(new_head) # add new head to snake
            game.slowDownStamina = 5
            if game.score % 10 == 0:
                game.apples.addApple(game)
        elif len(self.snake) < self.length:
            self.snake.append(new_head) # add new head to snake
            # Dont remove tail so snake grows to length at start
        else:
            # snake moves
            self.snake.append(new_head) # add new head to snake
            self.snake.pop(0) # remove tail

        if game.spacebarIsPressed:
            game.slowDownStamina -= 1
            if game.slowDownStamina <= 0:
                game.slowDownStamina = 0

        self.head = new_head
        self.hasMovedAfterDirectionChange = True


    def draw(self, screen, grid):
        for segment in self.snake:
            grid.drawSquare(screen, segment[0], segment[1], ("DarkGreen") if segment == self.head else ("Green"))


    def getKeyPressesFromEvent(self, event):
        if event.type == pygame.KEYDOWN:
            validKeys = [pygame.K_s, pygame.K_w, pygame.K_a, pygame.K_d]
            if not self.keyPresses and event.key in validKeys and not (self.simulateChangeDirection(event.key) == self.direction.getOpposite() or self.simulateChangeDirection(event.key) == self.direction):
                self.keyPresses.append(event.key)
            elif self.keyPresses and event.key in validKeys and len(self.keyPresses) < 3:
                self.keyPresses.append(event.key)

            # remove duplicate keys
            self.keyPresses = [k for k, _ in itertools.groupby(self.keyPresses)]


    def updateDirection(self):
        keyUP = pygame.K_w
        keyDOWN = pygame.K_s
        keyLEFT = pygame.K_a
        keyRIGHT = pygame.K_d

        if self.keyPresses:
            if self.keyPresses[0] == keyUP and self.direction != Direction.Direction.DOWN:
                self.direction = Direction.Direction.UP
            elif self.keyPresses[0] == keyDOWN and self.direction != Direction.Direction.UP:
                self.direction = Direction.Direction.DOWN
            elif self.keyPresses[0] == keyLEFT and self.direction != Direction.Direction.RIGHT:
                self.direction = Direction.Direction.LEFT
            elif self.keyPresses[0] == keyRIGHT and self.direction != Direction.Direction.LEFT:
                self.direction = Direction.Direction.RIGHT
            self.keyPresses.pop(0)
        self.hasMovedAfterDirectionChange = False

    def simulateChangeDirection(self, key):
        keyUP = pygame.K_w
        keyDOWN = pygame.K_s
        keyLEFT = pygame.K_a
        keyRIGHT = pygame.K_d
        if key == keyUP:
            return Direction.Direction.UP
        elif key == keyDOWN:
            return Direction.Direction.DOWN
        elif key == keyLEFT:
            return Direction.Direction.LEFT
        elif key == keyRIGHT:
            return Direction.Direction.RIGHT