
import pandas as pd
import re
from src.lib.layout.base import Layout, LayoutMapper

class LocalLayoutMapper(LayoutMapper):
  
  def __init__(self, layout_file:str):
    self.layout_file = layout_file

    lineas = open(self.layout_file, 'r').read().splitlines()

    filas = []

    fila_actual = []
    dentro_valor_largo = False
    encabezados = None  # Para almacenar los encabezados

    for linea in lineas:
      if linea.startswith('---'):
        continue

      columnas = linea.split('|')[1:-1]
      columnas = [col.strip() for col in columnas]

      # Identificar los encabezados
      if not encabezados and not columnas[0].isdigit() and any(columnas):
        encabezados = columnas  # Primera fila no numerada será los encabezados
        continue

      if columnas[0].isdigit():
        if fila_actual:
          filas.append(fila_actual)
        fila_actual = columnas
      else:
        for i, col in enumerate(columnas):
          if col:
            fila_actual[i] += ' ' + col

    if fila_actual:
        filas.append(fila_actual)
        
        
    def is_mv(column):
      
      if 'MV' in column:
        return True
      else :
        return False
      
    def is_sv(column):
      
      if 'SV' in column:
        return True
      else :
        return False
            
    def get_mv_key(column):
      
      column = column.lower()
      
      if 'mv por att' in column and 'sv por att' not in column:
        return int(re.sub(r'\D', '',column))
      elif 'mv por att' in column and 'sv por att' in column:
        return int(re.sub(r'\D', '',column.split('y')[0]))
      else :None
    
    
    def get_sv_key(column):
      
      column = column.lower()
      
      if 'mv por att' not in column and 'sv por att' in column:
        return int(re.sub(r'\D', '',column))
      elif 'mv por att' in column and 'sv por att' in column:
        return int(re.sub(r'\D', '',column.split('y')[1]))
      else :None
      
      
    def snake_case_transform(column):
      column = re.sub('\s{2,}', ' ', column).replace("'","").replace('.', '').replace(',',' ').replace('#','').replace('"','').replace('(','').replace(')','').replace('%','PC').replace('<','').replace('>','').replace('/',' ').replace(' ','_').lower().replace('__','_').replace('__','_')
      column = column.strip('_').replace(':','_').replace('-','_').replace('___','').replace('libre','').replace('=','_').replace('__','_').replace('sin_descripcion','').replace('recsubsecuente_bontecxinc','')
      return column
    
    def set_null(column):   
      if column == '':
        return None
      else:
        return column
    
          
    # Crear el DataFrame de pandas
    df = pd.DataFrame(filas, columns=['att','name','format','vinculation','observations'])
    df = df.astype(dtype={'att':'int','name':'str','format':'str','vinculation':'str','observations':'str'})
    df = df.drop(columns=['format','vinculation','observations'])
    df['name'] = df['name'].apply(snake_case_transform)
    df['name'] = df['name'].apply(set_null)
        
    table = df.to_dict(orient='records')
    
    new_table = []
    for record in table:
      name = ''
      if record['name'] is None:
        name = 'vacio_'+str(record['att'])
      else:
        name = record['name']
        
      new_record = {    
        'att': record['att'],
        'name': name,
      }
      new_table.append(new_record)
        
        
    df = pd.DataFrame.from_dict(new_table)
    
    self.layout = Layout(df)
    
  def get_layout(self)->Layout:
    return self.layout
  
  
