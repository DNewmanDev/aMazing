# aMazing - Algorithmic Maze Generation & Solution Visualization #

This advanced Python application uses recursive backtracking to generate random mazes and depth-first searching to solve them. Features real-time Tkinter visualization and step-by-step algorithm animation.

## 🚀 Key Features

- **Recursive Maze Generation**: Implements the recursive backtracking algorithm for maze creation
- **Intelligent Pathfinding**: Depth-first search algorithm with visual path tracking
- **Real-Time Visualization**: Tkinter-based GUI with smooth animation and color-coded paths
- **Algorithm Animation**: Step-by-step visualization of both generation and solving processes
- **Interactive Graphics**: Custom graphics engine with coordinate system management
  
## 🎯 Skills Demonstrated

- **Algorithm Implementation**: Classic CS algorithms (backtracking, DFS) with proper recursion
- **Data Structures**: 2D arrays, grid navigation, and state management
- **Object-Oriented Design**: Clean class hierarchies and encapsulation
- **GUI Programming**: Event-driven interfaces with real-time updates
- **Recursive Programming**: Deep understanding of recursive problem-solving patterns
- **Testing**: Unit test coverage for algorithm correctness
- **Mathematical Modeling**: Coordinate systems and geometric calculations

## 🏗️ Technical Architecture

### Algorithmic Design
- **Recursive Backtracking**: Generates mazes by carving paths through a grid of walls
- **Depth-First Search**: Solves mazes using recursive exploration with backtracking
- **Grid-Based Representation**: 2D matrix of cell objects with wall state management
- **State Management**: Tracks visited cells and wall configurations throughout algorithms

### Object-Oriented Design
- **Cell-Based Architecture**: Each maze cell encapsulates wall states and drawing logic
- **Graphics Abstraction**: Window, Point, and Line classes for rendering management
- **Modular Components**: Separate concerns for maze logic, graphics, and algorithm execution


### Graphics System
- **Custom Tkinter Wrapper**: Object-oriented graphics abstraction layer
- **Coordinate System**: Point and line rendering with proper scaling
- **Animation Framework**: Timed rendering updates with configurable delays
- **Visual Feedback**: Color-coded paths (red for solution, grey for backtracking)


## 💻 Technologies Used

- **Python 3.8+**: Modern Python with object-oriented programming
- **Tkinter**: Native GUI framework for cross-platform visualization


## 🔧 Technical Highlights

### Recursive Backtracking Algorithm
```python
def _break_walls_r(self, i, j):
    """Generate maze using recursive backtracking"""
    current_cell = self._cells[i][j]
    current_cell.visited = True
    
    while True:
        neighbors = self._get_unvisited_neighbors(i, j)
        if not neighbors:
            self._draw_cell(i, j)
            return
            
        # Choose random neighbor and break walls
        direction = random.choice(neighbors)
        self._break_wall(i, j, direction)
        self._break_walls_r(next_i, next_j)
```

### Depth-First Search Solver
```python
def _solve_r(self, i, j):
    """Solve maze using recursive DFS with visualization"""
    current_cell = self._cells[i][j]
    current_cell.visited = True
    
    if i == self._num_cols - 1 and j == self._num_rows - 1:
        return True  # Reached exit
        
    # Try each possible direction
    for direction in self._get_valid_moves(i, j):
        self._draw_move(current_cell, next_cell)
        if self._solve_r(next_i, next_j):
            return True
        # Backtrack visualization
        self._draw_move(current_cell, next_cell, undo=True)
```



## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Tkinter (usually included with Python)

### Installation & Running
```bash
# Clone the repository
git clone https://github.com/DNewmanDev/aMazing.git
cd amazing

# Run the maze generator and solver
python3 main.py

# Run the test suite
python3 tests.py
```

### Customization
Modify `main.py` to adjust maze parameters:
```python
# Window dimensions
win = Window(1200, 1000)

# Maze size (18 rows × 20 columns)
maze = Maze(50, 50, 18, 20, 40, 40, win)
```


## 🏗️ Project Structure

```
mazesolver/
├── main.py          # Entry point and configuration
├── maze.py          # Core Maze class with algorithms
├── cell.py          # Cell representation and rendering
├── graphics.py      # Tkinter wrapper classes
├── tests.py         # Unit tests for maze logic
└── README.md        # This documentation
```

## 🧪 Testing

This project includes comprehensive unit tests covering:
- Maze initialization and grid setup
- Cell wall state management
- Algorithm correctness verification
- Graphics rendering functionality

```bash
# Run all tests
python3 tests.py

# Test specific components
python3 -m unittest tests.TestMaze.test_maze_create_cells
```

This project demonstrates advanced algorithmic thinking, recursive programming mastery, and the ability to create interactive visualizations of complex computer science concepts. It showcases skills valuable for roles requiring algorithm implementation or real-time graphic rendering.
