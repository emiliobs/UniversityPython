# click.py

from graphics import *

def main():
    win = GraphWin("Click Me!")
    for i in range(10): 
        p = win.getMouse()
        print(f"You clicked at: {p.getX()} ,  {p.getY()}")

main()
