#futval-graph.py
from graphics import *


def main():
    #Intrdoduction
    print("This program plots the growth of a 10-years Invesment.")

    #Get principal and interest rate
    principal = float(input("Enter the initail principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    #Create a graphics windows with labls on left edge
    win = GraphWin("Invesment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), "0.0K").draw(win)
    Text(Point(20, 180), "2.5K").draw(win)
    Text(Point(20, 130), "5.0K").draw(win)
    Text(Point(20, 80), "7.5K").draw(win)
    Text(Point(20, 30), "10.0K").draw(win)
    
    #Draw for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40,230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    
    #Draw bars for successive years
    for year in range(1, 11):
        #claculate value for the next year.
        principal = principal * (1 + apr)
        #draw bar for this value
        xll = year * 25 + 40
        height = principal + 0.02
        bar = Rectangle(Point(xll, 230), Point(xll+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
        
        input("Press <Enter> to quit.")
        win.close()
main()

