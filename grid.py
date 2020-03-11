from cell import Cell
from draw import Draw
from distances import Distances

class Grid: 
    def __init__(self, rows:int, columns:int):
        self.rows = rows
        self.columns = columns
        self.grid = self.prepareGrid()
        self.configureCels()
        self.distances = None
    
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


    def fetchCell(self, row, column):
        return self.grid[0][0]

    def configureCels(self):
        for cell in self.eachCell():
            row = cell.row
            col = cell.column

            cell.north = self.isBoundary(row - 1, col)
            cell.south = self.isBoundary(row + 1, col)
            cell.west  = self.isBoundary(row, col - 1)
            cell.east  = self.isBoundary(row, col + 1)


    def isBoundary(self, row, column):
        if ((row >= 0 and row < self.rows) and (column >= 0 and column < self.columns)):
            return self.grid[row][column]
        return None
            

    def randomCell(self):
        row = randint(0, self.rows)
        column = randint(0,len(self.grid[row])-1)
        return self.grid[row][column]


    def size(self):
        self.rows * self.columns


    #  convert INT to string base 36
    def parseNumberHex(self, n):
        retStr = str(n).replace('0x', '')
        if len(retStr) == 1:
            revisedStr = retStr.rjust(len(retStr) + 1)
            return revisedStr.ljust(len(revisedStr) + 1)
        if len(retStr) == 2:
            return retStr.rjust(len(retStr)+1)
        
        return retStr


    def contents_of(self, cell):
        if cell in self.distances.cells:
            return self.parseNumberHex(hex(self.distances.cells[cell]))
            
        return "   " 


    def toString(self):
        
        # output = "+" + "---+" * self.columns + "\n"
        output = "+   +" + "---+" * (self.columns - 1) + "\n"
        
        for row in self.eachRow():
            output += "" 
            top = "|"
            bottom = "+"
            for cell in row:
                body = self.contents_of(cell) 
                east_boundary = " "    if cell.linkedTo(cell.east)  else "|"
                south_boundary = "   " if cell.linkedTo(cell.south) else "---"
                top += body + east_boundary
                corner = "+"
                bottom += south_boundary + corner
            output += top + "\n"
            output += bottom + "\n"

        print(output)
    

    def toDrawing(self):
        cellSize = 8
        fullSizeWidth = cellSize * self.columns
        fullSizeHeight = cellSize * self.rows
        
        d = Draw(fullSizeWidth, fullSizeHeight)
        # draw the north wall with the exit on the first cell
        d.drawLine(cellSize,0,fullSizeWidth,0)
        # draw the west wall
        d.drawLine(0,0,0,fullSizeHeight)

        for row in self.eachRow():
            for cell in row:

                X = cell.column * cellSize
                Y = cell.row * cellSize
                XV = X + cellSize
                YV = Y + cellSize 
                
                # horizontal
                # d.drawLine(X, YV, XV, YV)
                # vertical
                # d.drawLine(XV, Y, XV, YV)
                if not cell.linkedTo('east'):
                    d.drawLine(XV, Y, XV, YV)
                if not cell.linkedTo('south') and not (cell.south==None and cell.column==0):
                    d.drawLine(X, YV, XV, YV)
        
        d.closeWin()
