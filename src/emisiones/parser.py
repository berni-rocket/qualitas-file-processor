from src.lib.layout import LayoutMapper,Layout
import pandas as pd

class EmisionesParser:
  def __init__(self, mapper:LayoutMapper,data_file):
    self.mapper = mapper
    self.data_file = data_file

  def parse(self):

    layout_table = self.mapper.get_layout().get_table()
    
    file = open(self.data_file,'r',encoding='cp1252')
    
    table=[]
    for line in file:
      fields = line.split('þ')
      record = {}
      for column in layout_table:
        try:
          record[column['name']] = fields[column['att']]
        except:
          record[column['name']] = ''
      table.append(record)
      
    df = pd.DataFrame.from_dict(table)
    return df