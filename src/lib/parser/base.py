from abc import abstractmethod

from src.lib.layout.base import LayoutMapper

class Parser:
  
  @abstractmethod
  def __init__(self, mapper:LayoutMapper,data_file):
    pass

  @abstractmethod
  def get_subparser(self):
    pass