from DrawingManager import DrawingManager
from Game import Game
from Mark import Mark


d = DrawingManager()
mark = Mark(d)
game = Game(d, mark)
game.play()





