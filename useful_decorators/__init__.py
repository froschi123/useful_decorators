import datetime
import functools
import logging

print("================ Hallo Welt ========================")

# A decorator function that prints the time taken for a function call.
# if a logger is given as argument, the information will be printed in debug mode only
def measure_time_used(logger=None, log_mode=logging.DEBUG):
    """
    A decorator to print the time taken for a function call either with the print() function
    or using the logger given in the optional parameter
    :param logger: Optional, a logging.logger
    :param log_mode: defines the mode in which the information should be logged, either INFO or DEBUG
    :return: original function result
    """
    # We only do logging in DEBUG and INFO mode
    if logger is None:
        logger = logging.getLogger()
    log_func = logger.debug if log_mode == logging.DEBUG else logger.info if log_mode == logging.INFO else None

    def wrap(func):
        functools.wraps(func)

        # this function is used to calculate the time taken.
        # the parameters are used to hand over all parameters used to call the original function
        def inner_(*args, **kwargs):
            a = datetime.datetime.now()
            # here we call the original function which is known here, with the original parameters
            result = func(*args, **kwargs)
            b = datetime.datetime.now()
            time_taken = divmod((((b - a).seconds * 1000000) + (b - a).microseconds), 1000)[0]
            if log_func is not None:
                log_func("Call to '{}' took {} milliseconds.".format(func.__qualname__, time_taken))
            # we return the original result from the original function
            return result
        # we "only" call the timer function
        return inner_
    return wrap


# A decorator function that prints logs for a function call.
# if a logger is given as argument, the information will be printed in debug mode only
def log_call(logger=None, log_mode=logging.DEBUG):
    # We only do logging in DEBUG and INFO mode
    if logger is None:
        logger = logging.getLogger()
    """
    A decorator to print the time taken for a function call either with the print() function
    or using the logger given in the optional parameter
    :param logger: Optional, a logging.logger. If not set, a simple logger will be used
    :param log_mode: defines the mode in which the information should be logged, either INFO or DEBUG
    :return: original function result
    """
    # We only do logging in DEBUG and INFO mode
    log_func = logger.debug if log_mode == logging.DEBUG else logger.info if log_mode == logging.INFO else None

    def wrap(func):
        functools.wraps(func)

        def inner_(*args, **kwargs):
            if log_func is not None:
                log_func("--> Enter '{}' with args: {} and kwargs: {}"
                         .format(func.__qualname__, args, kwargs))
            # here we call the original function which is known here, with the original parameters
            a = datetime.datetime.now()
            result = func(*args, **kwargs)
            b = datetime.datetime.now()
            time_taken = divmod((((b - a).seconds * 1000000) + (b - a).microseconds), 1000)[0]
            if log_func is not None:
                log_func("<-- Leaving '{}' after {} milliseconds with result '{}'"
                         .format(func.__qualname__, time_taken, str(result)))
            # we return the original result from the original function
            return result
        # we "only" call the timer function
        return inner_
    return wrap


# A decorator giving detail descriptions of the parameters
def describe_params(logger=None, log_mode=logging.DEBUG):
    # We only do logging in DEBUG and INFO mode
    if logger is None:
        logger = logging.getLogger()
    # We only do logging in DEBUG and INFO mode
    log_func = logger.debug if log_mode == logging.DEBUG else logger.info if log_mode == logging.INFO else None
    param_position = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"]

    def wrap(func):
        functools.wraps(func)

        def inner_(*args, **kwargs):
            if log_func is not None:
                if len(args) > 0 or len(kwargs) > 0:
                    log_func("Describing parameters of call to '{}'".format(func.__qualname__))
                    pos = 0
                    for arg in args:
                        log_func("    {} parameter has type {} with value '{}'"
                                 .format(param_position[pos], type(arg), arg))
                        pos += 1
                    for kwarg in kwargs:
                        log_func("    {} parameter has type {} with value '{}'"
                                 .format(param_position[pos], type(kwarg), kwarg))
                        pos += 1
                else:
                    log_func("Enter '{}' without parameters".format(func.__qualname__))
            # here we call the original function which is known here, with the original parameters
            result = func(*args, **kwargs)
            # we return the original result from the original function
            return result
        # we "only" call the timer function
        return inner_
    return wrap


def debug_info(logger=None, log_mode=logging.DEBUG):
    # We only do logging in DEBUG and INFO mode
    if logger is None:
        logger = logging.getLogger()
    log_func = logger.debug if log_mode == logging.DEBUG else logger.info if log_mode == logging.INFO else None
    param_position = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"]

    def wrap(func):
        functools.wraps(func)

        def inner_(*args, **kwargs):
            if log_func is not None:
                if len(args) > 0 or len(kwargs) > 0:
                    log_func("Enter '{}' with parameters.".format(func.__qualname__))
                    pos = 0
                    for arg in args:
                        log_func("    {} parameter has type {} with value '{}'"
                                 .format(param_position[pos], type(arg), arg))
                        pos += 1
                    for kwarg in kwargs:
                        log_func("    {} parameter has type {} with value '{}'"
                                 .format(param_position[pos], type(kwarg), kwarg))
                        pos += 1
                else:
                    log_func("Enter '{}' without parameters".format(func.__qualname__))

            a = datetime.datetime.now()
            # here we call the original function which is known here, with the original parameters
            result = func(*args, **kwargs)
            b = datetime.datetime.now()
            time_taken = divmod((((b - a).seconds * 1000000) + (b - a).microseconds), 1000)[0]
            log_func("Leaving '{}' after {} milliseconds with result '{}'"
                     .format(func.__qualname__, time_taken, str(result)))
            # we return the original result from the original function
            return result
        # we "only" call the timer function
        return inner_
    return wrap
