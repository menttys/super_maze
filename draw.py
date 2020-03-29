from graphics import *

SPACING = {'left': 50, 'right': 50, 'top': 100, 'bottom': 100 }

class Draw:
  def __init__(self, width, height):
    self.title = "The Super Maze"
    self.height = height + SPACING['top'] + SPACING['bottom']
    self.width = width + SPACING['left'] + SPACING['right']
    self.win = GraphWin(self.title, self.width, self.height)
    self.setTitle()
  
  def setTitle(self):
    label = Text(Point(self.width/2, SPACING['top'] /2), self.title)
    label.draw(self.win)
    label.setTextColor('cyan')
    label.setStyle('bold')
    label.setSize(20)

  def drawWall():
    print("---")

  def drawLine(self, fx, fy, sx, sy):
    FX = SPACING['left'] + fx
    FY = SPACING['top'] + fy
    SX = SPACING['left'] + sx
    SY = SPACING['top'] + sy

    L = Line(Point(FX , FY), Point(SX, SY))
    L.setWidth(2)
    L.draw(self.win)

  def drawRectangle(self, fx, fy, sx, sy):
    FX = SPACING['left'] + fx
    FY = SPACING['top'] + fy
    SX = SPACING['left'] + sx
    SY = SPACING['top'] + sy

    poly_points = []
    Rect = Rectangle(Point(FX , FY), Point(SX, SY))
    Rect.setFill('#5577FF')
    Rect.setWidth(0)
    Rect.draw(self.win)

  def closeWin(self):
    self.win.getMouse() 
    self.win.close()    # Close window when done
