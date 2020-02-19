from cell import Cell

class Grid: 
    def __init__(self, rows:int, columns:int):
        self.rows = rows
        self.columns = columns
        self.links = {}
        self.topMaze = "+---"
        self.endTopMaze = "+"
        self.wall = "|   "
        self.endWall = "|"


    # setting the grid Array
    def setGridList(self):
        
        rowsList = [str("")] * self.rows
        wallList = [str("")] * self.rows  

        for R in range(0, self.rows):
            newLine = ""
            newWall = ""
            for C in range(0, self.columns):
                if C < (self.columns - 1):
                    newLine = newLine + self.topMaze
                    newWall = newWall + self.wall 
                else:
                    newLine = newLine + self.endTopMaze
                    newWall = newWall + self.endWall

            rowsList[R] = newLine    
            wallList[R] = newWall    
        
        return {
            "rowsList": rowsList,
            "wallList": wallList
        }


    def setGrid(self):
        theMaze = self.setGridList()

        for i in range(0, self.rows):
            print(theMaze["rowsList"][i])
            print(theMaze["wallList"][i])



    # print the results
    def printResult(self):
        print("================")
        self.setGrid()
        print("================")



myObj = Grid(4, 7)
myObj.printResult()

newCell = Cell(2,2)
newCell.printSomething()
newCell.link(1, True)