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
        distancesList = Distances(self)
        frontier = [self]

        print("-=-=-=-=-=-=-=-=-=-=-=-=-")
        i = 0
        while i < len(frontier):
            for cell in frontier:
                print(cell.links)
                for neighbor in cell.links:
                    print(distancesList.printList(cell))
                    # distancesList[neighbor] = distancesList[cell]
        #             new_frontier.append(neighbor)
        #     frontier = new_frontier
            i+=1

        return distancesList
