import Direction
import pygame

class Snake:
    snake = []
    direction = Direction.Direction.RIGHT
    length = 1
    hasMovedAfterDirectionChange = False

    def __init__(self, length):
        self.head = (5, 5)  # starting position
        self.snake = [self.head]  # snake body list
        self.length = length

        self.hasMovedAfterDirectionChange = False

    def move(self, game):
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
            # Dont remove tail so snake grows
            if game.score % 10 == 0:
                game.apples.addApple(game)
        elif len(self.snake) < self.length:
            self.snake.append(new_head) # add new head to snake
            # Dont remove tail so snake grows to length at start
        else:
            # snake moves
            self.snake.append(new_head) # add new head to snake
            self.snake.pop(0) # remove tail

        self.head = new_head
        self.hasMovedAfterDirectionChange = True


    def draw(self, screen, grid):
        for segment in self.snake:
            grid.drawSquare(screen, segment[0], segment[1], ("DarkGreen") if segment == self.head else ("Green"))


    def updateDirectionFromEvent(self, event):
        if event.type == pygame.KEYDOWN:
            keyPressed = event.key
            keyUP = pygame.K_w
            keyDOWN = pygame.K_s
            keyLEFT = pygame.K_a
            keyRIGHT = pygame.K_d
            if self.hasMovedAfterDirectionChange:
                # check if snake moved once before allowing direction change
                if keyPressed == keyUP and self.direction != Direction.Direction.DOWN:
                    self.direction = Direction.Direction.UP
                elif keyPressed == keyDOWN and self.direction != Direction.Direction.UP:
                    self.direction = Direction.Direction.DOWN
                elif keyPressed == keyLEFT and self.direction != Direction.Direction.RIGHT:
                    self.direction = Direction.Direction.LEFT
                elif keyPressed == keyRIGHT and self.direction != Direction.Direction.LEFT:
                    self.direction = Direction.Direction.RIGHT
            self.hasMovedAfterDirectionChange = False