from grid import Grid 
from binary_tree import BinaryTree 

grid = Grid(5, 5)
BinaryTree(grid)
# startig at the cell [0,0]
startCell = grid.fetchCell(0,0)
print(startCell)
distances = startCell.distances()
grid.distances = distances

grid.toString()