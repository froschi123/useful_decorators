# useful_decorators

This package contains some useful decorators for debugging and logging reasons.

### debug_info
debug_info logs some useful debug information for the function called.
The output may look like this:

    --> Enter 'my_function' with parameters.
        1st parameter has type <class 'int'> with value '0'
        2nd parameter has type <class 'int'> with value '3'
        3rd parameter has type <class 'str'> with value 'name'
        4th parameter has type <class 'str'> with value 'age'
    <maybe additional output created during call of my_function>
    <-- Leaving 'my_function' after 1601 milliseconds with result 'ok'

##### Parameters
- logger: The logger used to log the output.
- log_mode: The log level used to log the output. 

If logger is not set, a std-logger is being created:
    
    if logger is None:
        logger = logging.getLogger()

If log_mode is not set, logging.DEBUG will be used.

### measure_time_used
measure_time_used measures the time consumes by a function call. The output may look like this:

    Call to 'my_function' took 1601 milliseconds.
##### Parameters
- logger: The logger used to log the output.
- log_mode: The log level used to log the output. 

If logger is not set, a std-logger is being created:
    
    if logger is None:
        logger = logging.getLogger()

If log_mode is not set, logging.DEBUG will be used.

### log_call
log_call logs the call of a function like this:

    --> Enter 'my_function' with args: 123 and kwargs: {'name': 'Jane Doe'}
    <maybe additional output created during call of my_function>
    <-- Leaving 'my_function' after 1601 milliseconds with result 'True'

##### Parameters
- logger: The logger used to log the output.
- log_mode: The log level used to log the output. 

If logger is not set, a std-logger is being created:
    
    if logger is None:
        logger = logging.getLogger()

If log_mode is not set, logging.DEBUG will be used.

### describe_params
describe_params logs some useful debug information about parameters in a function call.
The output may look like this:

    Describing parameters of call to 'fourth_function'
        1st parameter has type <class 'str'> with value 'Some months'
        2nd parameter has type <class 'int'> with value '678'
        3rd parameter has type <class 'tuple'> with value '('Jun', 'July', 'August')'

##### Parameters
- logger: The logger used to log the output.
- log_mode: The log level used to log the output. 

If logger is not set, a std-logger is being created:
    
    if logger is None:
        logger = logging.getLogger()

If log_mode is not set, logging.DEBUG will be used.