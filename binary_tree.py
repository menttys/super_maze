from cell import Cell
from grid import Grid

# import random  
import random 

def render(grid):
    for cell in grid.eachCell():
        neighbors = []
        
        if cell.south:
            # neighbors.append(cell.north)
            neighbors.append('south')
        if cell.east:
            # neighbors.append(cell.east)
            neighbors.append('east')
        
        if len(neighbors) > 0:
            neighbor = random.choice(neighbors)
            if neighbor:
                cell.link(neighbor)  

    grid.toString()

render(Grid(4,4))


