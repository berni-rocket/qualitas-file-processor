from src.lib.layout.base import LayoutMapper
from src.lib.parser.base import Subparser
import pandas as pd
import boto3
import io

class S3Parser:
  def __init__(self, mapper:LayoutMapper,data_file):
    self.mapper = mapper
    self.data_file = data_file

  def get_subparser(self)->Subparser:
    
    bucket_name = self.data_file.replace('s3://','').split('/')[0]
    file_key = '/'.join(self.data_file.replace('s3://','').split('/')[1:])
    
    s3 = boto3.client('s3') 
    file_object = s3.get_object(Bucket=bucket_name,Key=file_key) 
    lines = file_object['Body'].read().decode('cp1252').splitlines()
    
    layout_table = self.mapper.get_layout().get_table()
    
    table=[]
    for line in lines:
      fields = line.split('þ')
      record = {}
      for column in layout_table:
        try:
          record[column['name']] = fields[column['att']]
        except:
          record[column['name']] = ''
      table.append(record)
      
    df = pd.DataFrame.from_dict(table)
    return Subparser(df)