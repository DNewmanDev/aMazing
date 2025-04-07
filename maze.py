from cell import Cell
import time
import random
class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self._x1 = x1
        self._y1 =y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self.seed=0

      
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)

    def _create_cells(self):
     
   # cell logic for this would be x1, x1 + cell_sizex1, ect w y
        for i in range (self._num_cols):
            topcol = []
            if self._num_rows == 0:
                raise ValueError('no rows here')
            for j in range (self._num_rows):
                topcol.append(Cell(self._win))
            self._cells.append(topcol)

        for i in range(self._num_cols):
            for j in range (self._num_rows):
                self._draw_cell(i,j)
    

        
        # make a list of columns for num cols
        # for every row, append a cell to the nested list 
        #upon completion, loop through completed matrix and use self._draw_cell

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        
        x1 = self._x1 + i * self._cell_size_x
        x2 = x1 + self._cell_size_x

        y1 = self._y1 + j * self._cell_size_y
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()


    def _animate(self):
        if self is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)

        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1,self._num_rows-1)



    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while True:
            possible_cells = []
            if j > 0 and self._cells[i][j-1].visited==False: ##IF TOP HASN'T BEEN VISITED
                possible_cells.append((i,j-1) )
            if j < self._num_rows - 1 and self._cells[i][j+1].visited==False: ##IF BOTTOM HASN'T BEEN VISITED
                possible_cells.append((i,j+1) )
            if i>0 and self._cells[i-1][j].visited==False: ##IF LEFT  HASN'T BEEN VISITED
                possible_cells.append((i-1,j) )
            if i < self._num_cols -1 and self._cells[i+1][j].visited==False: ##IF RIGHT HASN'T BEEN VISITED
                possible_cells.append(((i+1),j) )

            if len(possible_cells)==0:
                self._draw_cell(i,j)
                return

            random_cell_choice = random.randrange(len(possible_cells))
            next_cell = possible_cells[random_cell_choice]

            if next_cell[0] == i + 1: ##right
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False


            if next_cell[0] == i - 1: ##left
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False

            if next_cell[1] == j + 1: #bottom
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False

            if next_cell[1] == j - 1: ##top
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False

            self._break_walls_r(next_cell[0], next_cell[1])