import Game
import WallList

game = Game.Game(border=False)
game.run()

game2WallList = WallList.WallList((13, 13), (13, 11), (11, 13), (11, 11))
game2 = Game.Game(border=True, wallsAsWallList=game2WallList)
game2.run()