from distances import Distances

class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.links = {
            'north': False,
            'south': False,
            'east': False,
            'west': False
        }
        self.north: None
        self.south: None
        self.east: None
        self.west: None


    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            self.link(cell, False) 


    def unlink(self, cell, bidi=True):
        self.links.pop(cell)
        if bidi:
            self.unlink(cell, False)


    def linkedTo(self, side):
        if self.links[side]:
            return True
        
        return False
        

    def links(self):
        return self.links


    def neighbors(self):
        neighborsList = []

        if self.links['north']:
            neighborsList.append(self.north)
        if self.links['south']:
            neighborsList.append(self.south)
        if self.links['east']:
            neighborsList.append(self.east)
        if self.links['west']:
            neighborsList.append(self.west)
        
        return neighborsList


    def distances(self):
        distancesList = Distances(self)
        frontier = [self]
        
        # i = 0
        # while i < len(frontier):
        #     for cell in frontier:
        #         for neighbor in cell.neighbors():
        #             distancesList[neighbor] = distancesList[cell]
        #             new_frontier.append(neighbor)
        #     frontier = new_frontier
        #     i+=1

        return distancesList
