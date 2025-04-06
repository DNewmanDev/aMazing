from tkinter import Tk, BOTH, Canvas

class Window: #ROOT, WHICH IS THE BASE TK, CANVAS, WHICH IS THE GUI BOX, ISRUNNING FOR LOGIC
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("MazeSolver :D")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand = 1)
        self.__windowIsRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    # REDRAW WAITFORCLOSE AND CLOSE ARE LOGIC METHODS TO KEEP WINDOW RUNNING
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.__windowIsRunning = True
        while self.__windowIsRunning == True:
            self.redraw()


            
    #DRAWING THE LINES FOR MAZE GENERATION
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


    def close(self):
        self.__windowIsRunning = False


class Point:#MAY SEND THESE TO SEPERATE FILE
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, pta, ptb):
        self.pta = pta
        self.ptb = ptb
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.pta.x, self.pta.y, self.ptb.x, self.ptb.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, win): 
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
   
   
    # TOP LEFT TO TOP RIGHT x1,y1 TO x2, y1
    # TOP LEFT TO BOTTOM LEFT x1,y1 to x1, y2
    #BOTTOM LEFT TO BOTTOM RIGHT x1, y2 to x2, y2
    #TOP RIGHT TO BOTTOM RIGHT x2, y1 to x2, y2

    def draw(self, x1,y1,x2,y2 ):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

