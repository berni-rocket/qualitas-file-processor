import io
import boto3
from src.lib.process import ProcessHandler
from src.lib.process import Process
from src.emisiones.layout import LayoutMapper
import pandas as pd


class EmisionesProcess(Process):
  name = 'emisiones'
  
class EmisionesHandler(ProcessHandler):
  
  def __init__(self,mapper:LayoutMapper):
    self.mapper = mapper
    self.name = 'emisiones'
  
  def execute(self, process: Process) -> None:
    
    self.mapper.get_layout().to_csv('s3://data-qualitas/layout.csv',index=False)
    
    bucket_name = process.get_bucket_name()  
    file_key = process.get_file_key()
    
    s3 = boto3.client('s3') 
    file_object = s3.get_object(Bucket=bucket_name,Key=file_key) 
    file_content = file_object['Body'].read()
    file = io.BytesIO(file_content)

    count = 0
    for line in file:
      if count == 0:
        
        decoded_line = get_decoded_lines(line)
        fields = get_fields(decoded_line)
        decode_fields(self.mapper,fields)

        
        count += 1


