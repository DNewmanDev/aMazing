from tkinter import Tk,BOTH, Canvas
from graphics import Window, Line, Point
def main():
    win = Window(800,600)
    l = Line(Point(25,30), Point(444,666))
    win.draw_line(l,"black")
    win.draw_line(Line(Point(10,20), Point(10,600)),"black")
    win.wait_for_close()


if __name__ == "__main__":
    main()  