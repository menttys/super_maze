import random 
from cell import Cell

def BinaryTree(grid):
    for cell in grid.eachCell():
        neighbors = []

        if cell.links['south']['position']:
            neighbors.append('south')
        if cell.links['east']['position']:
            neighbors.append('east')
        
        if len(neighbors) > 0:
            neighbor = random.choice(neighbors)
            if neighbor:
                cell.link(neighbor)  





