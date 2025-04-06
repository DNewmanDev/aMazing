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
        if self._win is None:
            return
        if x1 >= x2 or y1 >=y2: #gaurd logic to make sure draw move function works
            raise ValueError('Invalid cell boundaries')
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

    def get_center(self): #for draw_move
        return ((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)

    def draw_move(self, to_cell, undo=False): #GAURD AGAINST INVALID INPUT
        if any(value is None for value in [self._x1, self._x2, self._y1, self._y2, 
                                   to_cell._x1, to_cell._x2, to_cell._y1, to_cell._y2]):
            raise ValueError("Invalid cell or target cell boundaries.")
        self_centerx, self_centery = self.get_center()
        to_cell_centerx, to_cell_centery = to_cell.get_center()
        line = Line(Point(self_centerx, self_centery), Point(to_cell_centerx, to_cell_centery))
        if undo==True:
            self._win.draw_line(line, fill_color="grey")
        else: 
            self._win.draw_line(line, fill_color="red")