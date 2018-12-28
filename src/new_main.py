from DrawingManager import DrawingManager
from MultipleDrawingManager import MultipleDrawingManager
from Game import Game
from Mark import Mark


d = DrawingManager()
# d = MultipleDrawingManager()
mark = Mark(d)
game = Game(d, mark)
game.play()





