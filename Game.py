import pygame
import Direction
import Grid
import Snake
import AppleList
import WallList

class Game:
    def __init__(self, border=False, wallsAsWallList=WallList.WallList()):
        self.grid = Grid.Grid(25, 25, 25, (212, 222, 151), (198, 204, 135), 50)
        self.snake = Snake.Snake(5)
        self.snake2 = Snake.Snake(5)
        self.apples = AppleList.AppleList()
        self.direction = Direction.Direction.UP
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0
        self.border = border
        self.walls = wallsAsWallList
        self.spacebarIsPressed = False

        self.apples.addApple(self, count=2)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.grid.drawWholeGrid(self.screen)
        self.snake.draw(self.screen, self.grid)
        self.walls.draw(self)
        self.apples.draw(self.screen, self.grid)
        self.renderScore()
        pygame.display.update()
        self.clock.tick(5 if self.spacebarIsPressed else 10)

    def renderScore(self):
        font = pygame.font.Font(None, 36)
        scoreText = font.render(f"Score: {self.score}", True, "White")
        wallsText = font.render(f"Walls: {self.border}", True, "White")
        self.screen.blit(scoreText, (10, 10))
        self.screen.blit(wallsText, (200, 10))

    def quit(self):
        self.running = False

    def run(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                self.snake.getKeyPressesFromEvent(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.spacebarIsPressed = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.spacebarIsPressed = False
            self.snake.move(self)
            self.draw()


