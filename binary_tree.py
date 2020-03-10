import random 
from cell import Cell

def BinaryTree(grid):
    for cell in grid.eachCell():
        neighbors = []

        if cell.south:
            neighbors.append(cell.south)
        if cell.east:
            neighbors.append(cell.east)
        
        if len(neighbors) > 0:
            neighbor = random.choice(neighbors)
            if neighbor:
                cell.link(neighbor)  





