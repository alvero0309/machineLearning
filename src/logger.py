#Verificar documentación de logger

#Logger no permite almacenar la informacíón sobe la ejecución
#Nos permite cachar cualquier error , alguna exception

import logging
import os
from datetime import datetime

BASE_DIR = '/home/ale/Escritorio/Proyectos/machineLearning'
#El nombre del archivo log
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#Se obtiene con os.getcwd el workin directory y se crea una carpeta logs
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
#Crea un directorio
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    #Formato del mensaje
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

