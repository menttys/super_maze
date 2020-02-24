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


    def toString(self):
        
        output = "+" + "---+" * self.columns + "\n"
        
        for row in self.eachRow():
            output += "" 
            top = "|"
            bottom = "+"
            for cell in row:
                body = "   " # 3 spaces
                east_boundary = " " if cell.linkedTo('east')==True else "|"
                south_boundary = "   " if cell.linkedTo('south') else "---"
                top += body + east_boundary
                # south_boundary = "---"
                corner = "+"
                bottom += south_boundary + corner
            output += top + "\n"
            output += bottom + "\n"

        print(output)
