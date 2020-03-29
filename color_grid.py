from grid import Grid
from distances import Distances

class ColorGrid(Grid):
    def contents_of(self, cell):
        if self.distances:
            if cell in self.distances.cells:
                return self.parseNumberHex(hex(self.distances.cells[cell]))
            
        return "   " 