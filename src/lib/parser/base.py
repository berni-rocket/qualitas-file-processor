from abc import abstractmethod

from src.lib.layout.base import LayoutMapper
from src.utils import generate_combinations


class Subparser:
  
  def __init__(self,df):
    self.df = df
    
  def all(self):
    return self.df
  
  def peek(self,indexes:list):
    columns = [self.df.columns[i] for i in indexes]
    return self.df[columns]
  
  def expand(self,indexes:list,indexes_to_expand:list):
    columns = [self.df.columns[i] for i in indexes]
    columns_to_expand = [self.df.columns[i] for i in indexes_to_expand]
    
    return generate_combinations(df=self.df[columns+columns_to_expand],columns=columns,columns_to_expand=columns_to_expand)
    

class Parser:
  @abstractmethod
  def __init__(self, mapper:LayoutMapper,data_file):
    pass

  @abstractmethod
  def get_subparser(self)->Subparser:
    pass