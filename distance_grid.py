from grid import Grid
from distances import Distances

class DistanceGrid(Grid):
    def contents_of(self, cell):
        if cell in self.distances.cells:
            return self.parseNumberHex(hex(self.distances.cells[cell]))
            
        return "   " 