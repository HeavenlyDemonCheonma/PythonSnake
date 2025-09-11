import Game

game = Game.Game(border=False)
game.run()

game2 = Game.Game(border=True)
game2.walls.addWall((13, 13), (13, 11), (11, 13), (11, 11))
game2.run()