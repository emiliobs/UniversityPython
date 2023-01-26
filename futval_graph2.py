from graphics import *

def main():
    #Introduccion
    print("This program plots the grwth of a 10-year invesment.")
    
    #Get principal and interest rate
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    
    # Create a graphics windows with labels on left edge
    win = GraphWin("Insvestment Groeth Chart", 500, 500)
    win.setBackground("white")
    win.setCoords(-1.5, -200, 11.5, 10400)
    Text(Point(-1, 2500), "2.5K").draw(win)    
    Text(Point(-1, 5000), "5.0K").draw(win)
    Text(Point(-1, 7500), "7.5K").draw(win)
    Text(Point(-1, 10000), "10.0K").draw(win)

    #Draw bar for iniitial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    #Draw a bar for each subsequent year
    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.draw(win)

    input("Press <Enter> to quit.")
    win.close()

main()    

