class Process:
  
  name=''
  
  def __init__(self,bucket_name:str,file_key:str,params:dict={}):
    self.bucket_name = bucket_name
    self.file_key = file_key
    self.params = params
    
  def get_name(self)->str:
    return self.name
  
  def get_params(self)->dict:
    return self.params
  
  def get_bucket_name(self):
    return self.bucket_name
  
  def get_file_key(self):
    return self.file_key


class ProcessHandler:
  name=''
  def __init__(self):
    pass    
  def execute(self,process:Process)->None:
    pass
  def get_name(self)->str:
    return self.name
  

class ProcessBus:
  
  def __init__(self):
    self.handlers={}
    
  # agregamos handler en base a su nombre
  def add_handler(self,handler:ProcessHandler):
    self.handlers[handler.get_name()]=handler
    
  # obtenemos lista de handlers suscritos
  def get_handler_names(self)->list:
    return self.handlers.keys()
    
  def dispatch(self,process:Process):
        
    # en caso de no existir estar suscrito un handler para el proceso
    if process.get_name() not in self.handlers.keys():
      print(f"Process Named {process.get_name()} Not Found")
    
    # en caso de si estar suscrito ejecutamos
    else:
      self.handlers[process.get_name()].execute(process)
      