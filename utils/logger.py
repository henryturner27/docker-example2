from time import time

from config.logger import logger


def log_execution_time(func: callable):
    def wrapper(*args):
        start_time = time()
        func(*args)
        end_time = time()
        logger.debug(f'took {round(end_time-start_time, 2)}s')
    return wrapper
