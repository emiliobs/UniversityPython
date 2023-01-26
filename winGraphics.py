
from graphics import *


def main():
    win = GraphWin("Circle Clone", 400, 400)
    leftEye =  Circle(Point(80,50), 5)
    leftEye.setFill("yellow")
    leftEye.setOutline("red")
    #clone here
    rightEye = leftEye.clone() #rightEye is an exact copy of the leftEye
    rightEye.move(20, 0)
    leftEye.draw(win)
    rightEye.draw(win)


main()