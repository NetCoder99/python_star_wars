import logging
from typing import List
from models.json.film_json import film_json
from models.json.people_json import people_json
from utilities.json_loaders import load_all_files, load_json_from_file
from logging_utils        import logging_config

logging_config.config(logging.DEBUG)
logger = logging.getLogger("app_logger")

# ----------------------------------------------------------------------------------------
# multi-threaded data load processes
# ----------------------------------------------------------------------------------------
def load_data():
    # load all films to internal classes
    film_objects:List[film_json] = []
    film_objects.append(load_json_from_file('1.json', film_json))
    film_objects.append(load_json_from_file('2.json', film_json))
    film_objects.append(load_json_from_file('3.json', film_json))

    people_objects:List[people_json] = []
    people_objects.append(load_json_from_file('1.json', people_json))
    people_objects.append(load_json_from_file('2.json', people_json))
    people_objects.append(load_json_from_file('3.json', people_json))

    return "Loaded some data."


# ----------------------------------------------------------------------------------------
# main process to execute 
# ----------------------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        logger.info('=====================================')
        logger.info('Main - Started')
        logger.info('=====================================')
        
        #logger.info('load_data:{}'.format(load_data()))
        load_all_files()
        
        logger.info('=====================================')
        logger.info('Main - Finished')
        logger.info('=====================================')
    except Exception as ex:
        logger.info('=====================================')
        logger.info('Main - Failed')
        logger.info('=====================================')
        print("Error while executing applicaiton", ex)


