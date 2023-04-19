import time 

class Player:
  def __init__(self, pnum=1):
    """
    Initialize the player object
    args: pnum [int] the player's id number
    """
    self.player_num = pnum
    self.lives = 3 # players always start with 3 lives
    self.is_large = False # player always starts small

class Block:
  """
  Initializes blocks
  """
  def __init__(height, num) -> None:
    pass

class Text:
  """
  Initializes text in game
  """
  def __init__(font, size, position, color, msg="") -> None:
    pass

class Coins:
  def __init__(counter=int) -> None:
    pass

class Tubes:
  def __init__(color="green", accept_player=True) -> None:
    pass