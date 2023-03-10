#triangle.py


from graphics import *

def main():
    win = GraphWin("Draw a Trangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points") 
    message.draw(win)

    #Get and draw three verties of traingle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)


    # Use polygon object to draw the trangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.setWidth("5")
    triangle.draw(win)  

    #Wait for another click to exit
    message.setText("Click anywhere to quit")
    win.getMouse()

main()
    
     