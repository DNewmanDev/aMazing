from tkinter import Tk,BOTH, Canvas

def main():
    win = Window(800,600)
    win.wait_for_close()
    return None



class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("MazeSolver :D")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand = 1)
        self.__windowIsRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.__windowIsRunning = True
        while self.__windowIsRunning == True:
            self.redraw()
    
    def close(self):
        self.__windowIsRunning = False


if __name__ == "__main__":
    main()  