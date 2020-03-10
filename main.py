import random 
import sys
from grid import Grid
from binary_tree import BinaryTree

ROW = int(sys.argv[1])
COL = int(sys.argv[2])

def render(grid):
    BinaryTree(grid)
    grid.toString()
    # grid.toDrawing()

render(Grid(ROW,COL))