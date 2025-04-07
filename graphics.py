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
