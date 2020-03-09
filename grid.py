from cell import Cell
from draw import Draw

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
            cell.north = self.isBoundary(row - 1, col) 
            cell.south = self.isBoundary(row + 1, col)
            cell.west  = self.isBoundary(row, col - 1)
            cell.east  = self.isBoundary(row, col + 1)


    def isBoundary(self, row, column):
        if ((row >= 0 and row < self.rows) and (column >= 0 and column < self.columns)):
            return [row, column]
            


    def randomCell(self):
        row = randint(0, self.rows)
        column = randint(0,len(self.grid[row])-1)
        return self.grid[row][column]


    def size(self):
        self.rows * self.columns


    def contents_of(self, cell):
        print(cell.distances())
        return " 1 "
        # if distances and distances[cell]:
        #     distances[cell].toString(36)


    def toString(self):
        
        # def contents_of(cell):
        #     return "   " # 3 spaces

        # output = "+" + "---+" * self.columns + "\n"
        output = "+   +" + "---+" * (self.columns - 1) + "\n"
        
        for row in self.eachRow():
            output += "" 
            top = "|"
            bottom = "+"
            for cell in row:
                body = self.contents_of(cell) 
                east_boundary = " " if cell.linkedTo('east')  else "|"
                south_boundary = "   " if cell.linkedTo('south') else "---"
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
