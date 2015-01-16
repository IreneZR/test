
class Coord(object):
  
  """
  Represent Cartesian coordinates.
  """

  def __init__(self, x=0, y=0):
    self._x = x
    self._y = y
    

class Data(object):
  
  """
  Represent list of coordinates.
  """
  
  def __init__(self):
    self._data = []
