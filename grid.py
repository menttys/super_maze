from cell import Cell

class Grid: 
    def __init__(self, rows:int, columns:int):
        self.rows = rows
        self.columns = columns
        self.grid = self.prepareGrid()
        self.configureCels()
    
    def prepareGrid(self):
        newGrid = []
        for R in range(0, self.rows): 
            newRow = []
            for C in range(0, self.columns):   
                newRow.append(Cell(R, C))
            newGrid.append(newRow)
        return newGrid
        

    def eachRow(self):
        for row in range(self.rows):
            yield self.grid[row]


    def eachCell(self):
        for row in self.grid:
            for cell in row:
                yield cell   


    def configureCels(self):
        for cell in self.eachCell():
            row = cell.row
            col = cell.column
            cell.north = [row - 1, col]
            cell.south = [row + 1, col]
            cell.west  = [row, col - 1]
            cell.east  = [row, col + 1]


    def randomCell(self):
        row = randint(0, self.rows)
        column = randint(0,len(self.grid[row])-1)
        return self.grid[row][column]


    def size(self):
        self.rows * self.columns


    def printResult(self):
        print(self.grid)

        
# myObj = Grid(4, 4)
# myObj.printResult()
# print(myObj.grid[1]) 