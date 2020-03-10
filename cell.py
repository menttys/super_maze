from distances import Distances

class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.links = {
            'north': { 'hasNeighbor': False, 'cellRef': None, 'position': None },
            'south': { 'hasNeighbor': False, 'cellRef': None, 'position': None },
            'east':  { 'hasNeighbor': False, 'cellRef': None, 'position': None },
            'west':  { 'hasNeighbor': False, 'cellRef': None, 'position': None }
        }


    def link(self, side, bidi=True):
        self.links[side]['hasNeighbor'] = True
        # neighborCell = self.links[side]['cellRef']
        # if bidi:
        #     self.link(neighborCell, False) 


    def unlink(self, cell, bidi=True):
        self.links.pop(cell)
        if bidi:
            self.unlink(cell, False)


    def linkTheNeigbors(self, cell, side):
        # print(self.links[side])
        self.links[side]['cellRef'] = cell

        
    def linkedTo(self, side):
        if self.links[side]['hasNeighbor']:
            return True
        
        return False
        

    def links(self):
        return self.links


    # def findNeighbour(self):
    

    def neighbors(self):
        neighborsList = []

        if self.links['north']['hasNeighbor']:
            neighborsList.append(self.links['north']['cellRef'])

        if self.links['south']['hasNeighbor']:
            neighborsList.append(self.links['south']['cellRef'])

        if self.links['east']['hasNeighbor']:
            neighborsList.append(self.links['east']['cellRef'])

        if self.links['west']['hasNeighbor']:
            neighborsList.append(self.links['west']['cellRef'])
        

        return neighborsList


    def distances(self):
        distancesList = Distances(self)
        frontier = [self]

        i = 0
        # while i < len(frontier):
        #     for cell in frontier:
        #         for neighbor in cell.neighbors():
        #             print(neighbor)
                    # distancesList[neighbor] = distancesList[cell]
        #             new_frontier.append(neighbor)
        #     frontier = new_frontier
        #     i+=1

        return distancesList
