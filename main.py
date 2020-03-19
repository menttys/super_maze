import random 
import sys
from grid import Grid
from binary_tree import BinaryTree
from dijkstra import dijkstra

STL = ''
ROW = int(sys.argv[1])
COL = int(sys.argv[2])
    
if len(sys.argv) > 3 :
    STL = sys.argv[3] 

def draw(grid):
    grid.toDrawing()

def render(grid):
    BinaryTree(grid)
    grid.toString()
    grid.toDrawing()


if STL == 'dijk':
    dijkstra(ROW,COL)
else:
    render(Grid(ROW,COL))
    