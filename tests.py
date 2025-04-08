import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows, num_cols, 10, 10)

        self.assertEqual(len(m1._cells), num_cols,)
        self.assertEqual(len(m1._cells[0]), num_rows,)


    def test_maze_create_cells_none_cols(self):
        num_cols = None
        num_rows = 10
        with self.assertRaises(TypeError):
            m1 = Maze(0,0,num_rows, num_cols, 10, 10)

    
    def test_maze_create_cells_none_rows(self):
        num_cols = 5
        num_rows = None
        with self.assertRaises(TypeError):
            m1 = Maze(0,0,num_rows, num_cols, 10, 10)

    
    def test_maze_create_cells_none_all(self):
        num_cols = None
        num_rows = None
        with self.assertRaises(TypeError):
            m1 = Maze(0,0,num_rows, num_cols, 10, 10)

     
    def test_maze_create_cells_no_rows(self):
        num_cols = 12
        num_rows = 0
        with self.assertRaises(ValueError):
         m1 = Maze(0,0,num_rows, num_cols, 10, 10)


    def test_maze_break_EandE(self):
        num_cols = 10 
        num_rows = 10
        m1 = Maze(0,0,num_rows, num_cols, 10, 10)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[num_cols-1][num_rows-1].has_bottom_wall, False)

    def test_cell_reset(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows, num_cols, 10, 10)
        # self.assertEqual(m1._cells[int(num_cols/2)][int(num_rows/2)].visited, False)
        # self.assertEqual(m1._cells[11][9].visited, False)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(cell.visited, False)

if __name__ == "__main__":
    unittest.main()