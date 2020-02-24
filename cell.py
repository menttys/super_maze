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
        if self.links[side] and self.east[1] < 4:
            return True
        
        return False
        

    def links(self):
        return self.links

    
    def neighbors(self):
        neighborsList = []
        if self.north:
            neighborsList.append("north")
        if self.south:
            neighborsList.append("south")
        if self.east:
            neighborsList.append("east")
        if self.west:
            neighborsList.append("west")
        
        self.links = neighborsList