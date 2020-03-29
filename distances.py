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

    def printList(self, cell):
        print(self.cells[cell])

    def pathTo(self, goal):
        current = goal

        breadcrumbs = Distances(self.root)
        breadcrumbs.addDistanceCell(current, self.cells[current])
        
        print(current)
        print(self.root)
         
        while current == self.root:
            print("_____")
            for neighbor in current.links:
                print("_____")
                if self.cells[neighbor] < self.cells[current]:
                    print("_____")
                    breadcrumbs.addDistanceCell(neighbor, self.cells[neighbor])
                    current = neighbor
                    continue
        
        # return breadcrumbs

