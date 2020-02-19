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
            print(neighbor)
            # cell += neighbor


    output = "+" + "---+" * grid.columns + "\n"
    
    for row in grid.eachRow():
        output += "" 
        top = "|"
        bottom = "+"
        for cell in row:
            body = "   " # 3 spaces
            east_boundary = " " if cell.linkedTo() else "|"
            # top += body + east_boundary
            # south_boundary = "   " if cell.linked_to(cell.south) else "---"
            # east_boundary = "|"
            top += body + east_boundary
            south_boundary = "---"
            corner = "+"
            bottom += south_boundary + corner
        output += top + "\n"
        output += bottom + "\n"

    print(output)

# initMaze(Grid(4,4))
render(Grid(4,4))


