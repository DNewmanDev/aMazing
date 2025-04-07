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
        m1 = Maze(0,0,num_rows, num_cols, 10, 10)

        self.assertEqual(len(m1._cells), num_cols,)
        self.assertEqual(len(m1._cells[0]), num_rows,) #no cells in the colums



if __name__ == "__main__":
    unittest.main()