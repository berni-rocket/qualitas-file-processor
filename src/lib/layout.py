from abc import abstractmethod
import pandas as pd
import re


class Layout:
  
  def __init__(self,df):
    self.df = df
    
  def get_df(self):
    return self.df
  
  def get_table(self):
    return self.df.to_dict(orient='records')
  
  def get_names(self):
    return self.df['name'].tolist()
  
  
  
class LayoutMapper:
  
  @abstractmethod
  def __init__(self, layout_file:str):
    pass
  
  @abstractmethod
  def get_layout(self)->Layout:
    pass
  
  
