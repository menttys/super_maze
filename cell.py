from distances import Distances

class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.links = []
        self.north = None
        self.south = None
        self.east = None
        self.west = None    

    def link(self, cell, bidi=True):
        self.links.append(cell)
        if bidi:
            cell.link(self, False) 


    def unlink(self, cell, bidi=True):
        self.links.pop(cell)
        if bidi:
            self.unlink(cell, False)

        
    def linkedTo(self, cell):
        if cell in self.links:
            return True
        
        return False
        

    def links(self):
        return self.links
    

    def neighbors(self):
        neighborsList = []

        if self.north:
            neighborsList.append(self.north)

        if self.south:
            neighborsList.append(self.south)

        if self.east:
            neighborsList.append(self.east)

        if self.west:
            neighborsList.append(self.west)

        return neighborsList


    def distances(self):
        distance = Distances(self)
        frontier = [self]

        i = 0
        while frontier:
            new_frontier = []
            
            for cell in frontier:
                for neighbor in cell.links:
                    if neighbor in distance.cells:
                        continue
                    
                    # add a neighbor distance of the actuall cell + 1
                    distance.addDistanceCell(neighbor, distance.cells[cell] + 1 )
                    new_frontier.append(neighbor)
            frontier = new_frontier

        return distance
