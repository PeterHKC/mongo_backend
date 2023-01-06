import logging
import traceback
import sys

def __log_exception_message(exception_message, log_level = logging.ERROR):
    tb = traceback.extract_tb(sys.exc_info()[2])
    line_number = tb[-1][1]
    logging.log(log_level, f'File: {__file__}: {line_number}. Error: {exception_message}.')

def log_function(log_level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            logging.log(log_level, f'Arguments: {args}, {kwargs}')
            logging.log(log_level, f'Return value: {result}')
            return result
        return wrapper
    return decorator

def log_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            tb = traceback.extract_tb(sys.exc_info()[2])
            line_number = tb[-1][1]
            __log_exception_message(e)
    return wrapper