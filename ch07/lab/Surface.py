from Rectangle import Rectangle

class Surface:
  def __init__(self, filename, x, y, height, width):
    self.image = filename
    self.rect = Rectangle(x,y,height,width)

  def getRect(self):
    return self.rect
    