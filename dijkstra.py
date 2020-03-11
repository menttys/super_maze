import random 
import sys
from grid import Grid
from binary_tree import BinaryTree

ROW = int(sys.argv[1])
COL = int(sys.argv[2])

grid = Grid(ROW, COL)
BinaryTree(grid)

# startig at the cell [0,0]
startCell = grid.fetchCell(0,0)
distances = startCell.distances()
grid.distances = distances

grid.toString()