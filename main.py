from tkinter import Tk,BOTH, Canvas
from graphics import Window, Line, Point
def main():
    win = Window(800,600)
    win.wait_for_close()
    l = Line(Point(25,30), Point(444,666))
    win.draw_line(l,"black")
    win.wait_for_close()


if __name__ == "__main__":
    main()  