from datetime import datetime
import logging

from logging_utils.logging_handler import get_console_handler

now = datetime.now()
date_time_str = now.strftime("%Y%m%d_%H")

def config(log_level=logging.INFO, file_name:str=None):
    logging_formatter = logging.Formatter('%(asctime)s :: %(name)s :: %(threadName)s :: %(levelname)-9s :: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger("app_logger")
    logger.setLevel(log_level)

    console_handler = get_console_handler(logging_formatter, log_level)
    logger.addHandler(console_handler)

    #file_handler = get_file_handler('logs/{}.log'.format(file_name), logging_formatter, log_level)
    #logger.addHandler(file_handler)

    #sql_handler = sqlite_db_handler(database="log_data.db", table="app_logs")
    #logger.addHandler(sql_handler)
