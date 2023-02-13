import graphics
from graphics import * #makes methods available without prefix
win = GraphWin('Shapes')
center = Point(100,100)
circ = Circle(center, 30)
circ.setFill('red')
circ.draw(win)
