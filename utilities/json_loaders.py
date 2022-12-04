# ---------------------------------------------------------------
# for this app, all files will be relative to the run location 
# of the application. 
# ---------------------------------------------------------------
import json
import logging
from pathlib import Path
import os
import traceback

from models.json.abstract_loader import loadFromJson
from models.json.film_json import film_json

from multiprocessing import Process
#import multiprocessing

from models.json.people_json import people_json


# for this app, all files will be relative to the run location
# of the application. 
logger = logging.getLogger("app_logger")
parent_dir = Path(os.path.dirname(__file__)).parent 
json_data_path = os.path.join(parent_dir, 'data', 'json')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# instantiate the threaded objects and load the data
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def load_all_files():
    loader_types = [film_json, people_json]
    procs = []

    # load the processes array 
    logger.info("-----------------------------------------------")
    logger.info("--- Creating process array - started")
    for loader_type in loader_types:
        proc1 = Process(target=load_json_from_file, args=('1.json', loader_type))
        proc2 = Process(target=load_json_from_file, args=('2.json', loader_type))
        proc3 = Process(target=load_json_from_file, args=('3.json', loader_type))
        procs.append(proc1)
        procs.append(proc2)
        procs.append(proc3)

    # start all the threads
    logger.info("-----------------------------------------------")
    logger.info("--- Starting processes")
    for proc in procs:
        proc.start()

    # wait for all 'processing' threads to complete
    logger.info("-----------------------------------------------")
    logger.info("--- Waiting on processes - started")
    for proc in procs:
        proc.join()
    logger.info("-----------------------------------------------")
    logger.info("--- Waiting on processes - finished")


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# load data from the file and convert to a python object 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def load_json_from_file(file_name: str, loader_class: loadFromJson):
    try:
        logger.info(f'module:{loader_class.__module__}') 
        if 'film' in loader_class.__module__:
            dir_name = 'films'
        elif 'people' in loader_class.__module__:   
            dir_name = 'people'
        else:
            raise Exception("Unkown data type!")

        file_path = os.path.join(json_data_path, dir_name, file_name)
        logger.info('file_path:{}'.format(file_path)) 
        file_obj = open (file_path, "r", encoding="utf-8")
        json_str = json.loads(file_obj.read(), strict=False) 
        return loader_class.fromJson(json_str)

    except Exception as ex:
      logger.error(f'error:{ex} while reading: {file_path}')
      tb = traceback.format_exc()
      logger.error(f'stack trace:{tb}')
