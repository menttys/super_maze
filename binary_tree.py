from cell import Cell
from grid import Grid

# import random  
import random 

def render(grid):
    for cell in grid.eachCell():
        neighbors = []
        if cell.north:
            neighbors.append(cell.north)
        if cell.east:
            neighbors.append(cell.east)
        if len(neighbors) > 0:
            neighbor = random.choice(neighbors)
            neighbor.append(cell)


render(Grid(4,4))


