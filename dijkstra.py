import random 
import sys
from grid import Grid
from distance_grid import DistanceGrid
from binary_tree import BinaryTree

def dijkstra(ROW, COL):
    distanceGrid = DistanceGrid(ROW, COL)
    BinaryTree(distanceGrid)

    # startig at the cell [0,0]
    startCell = distanceGrid.fetchCell(0,0)
    distances = startCell.distances()
    distanceGrid.distances = distances
    distanceGrid.toString()
    
    print(":: Path from northwest corner to southwest corner ::")
    distanceGrid.distances = distances.pathTo(distanceGrid.fetchCell(distanceGrid.rows - 1,0))
    
    distanceGrid.toString()
    distanceGrid.toDrawing()