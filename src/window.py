import Tkinter as tk
from data import Coord
from data import Data


class Window(object):
  
  """
  Create window and visualize data.
  """
  
  def __init__(self):
    self._root = tk.Tk()
    self._data = Data()
    
  def draw_point(self, coord):
    pass
    
  def draw(self):
    pass
