class Distances:
    def __init__(self, root):
        self.root = root
        self.cells = {}
        self.cells[self.root] = 0

    def fetchDistanceCell(self, cell):
      return self.cells[cell]
    
    def addDistanceCell(self, cell, distance):
      self.cells[cell] = distance

    def allDistances(self):
      return self.cells

  

