import json

from src.lib.process import ProcessBus
from src.emisiones import EmisionesProcess,EmisionesHandler
from src.emisiones.layout import LayoutMapper

def lambda_handler(event, context):
    
  bus = ProcessBus()
  bus.add_handler(
    EmisionesHandler(
      mapper=LayoutMapper(
        bucket_name='data-inputs-qualitas',
        file_key='layouts/PV.txt',
        column_numbers=[
          0,
          1,
          3,
          4,
          5,
          6,
          7,
          8,
          11,
          12,
          13,
          14,
          15,
          19,
          21,
          22,
          23,
          24,
          25,
          26,
          27,
          28,
          29,
          30,
          31,
          32,
          35,
          37,
          44,
          45,
          46,
          52,
          56,
          57,
          61,
          62,
          63,
          65,
          67,
          68,
          69,
          78,
          79,
          80,
          81,
          82,
          95,
          97,
          98,
          99,
          100,
          101,
          102,
          103,
          104,
          105,
          106,
          107,
          108,
          122,
          147,
          163,
          164,
          165,
          166,
          178,
          179,
          190,
          197,
          242,
          290,
          293,
          294,
          385
        ]
      )
    )
  )

  for record in event['Records']: 

    # obtenemos nombre del bucket
    bucket_name = record['s3']['bucket']['name'] 
    
    # obtenemos nombre del archivo
    file_key = record['s3']['object']['key'] 
    
    process = EmisionesProcess(bucket_name=bucket_name,file_key=file_key)
    
    bus.dispatch(process=process)