from distance_grid import DistanceGrid 
from binary_tree import BinaryTree 

grid = DistanceGrid(5, 5)
BinaryTree(grid)
start = grid[0, 0]
# distances = start.distances
# grid.distances = distances
print(grid)