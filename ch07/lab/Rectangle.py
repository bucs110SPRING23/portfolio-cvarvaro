#from Surface import Surface

class Rectangle:
  def __init__(self, x, y, height, width):
    self.x = abs(x)
    self.y = abs(y)
    self.height = abs(height)
    self.width = abs(width)

def __str__(self):
  return f"({self.x}, {self.y}, {self.height}, {self.width})"