import json

from src.lib.layout.s3 import S3LayoutMapper
from src.lib.parser.s3 import S3Parser

def lambda_handler(event, context):
  
  df = S3Parser(mapper=S3LayoutMapper('s3://data-qualitas/layouts/PV.txt'),data_file='s3://data-inputs-qualitas/pv/PV.txt').get_subparser().all()
        
  for record in event['Records']: 

    # obtenemos nombre del bucket
    bucket_name = record['s3']['bucket']['name'] 
    
    # obtenemos nombre del archivo
    file_key = record['s3']['object']['key'] 
    
    
