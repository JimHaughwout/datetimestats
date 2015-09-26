"""
TODO: Explanation of why we do not validate the entire list every time we call
"""

def validate_operand(input, function_name):
    """TODO: Ensures passed valid input"""
    if not isinstance(input, list): 
        raise TypeError('unsupported operand for %s, requires list of datetimes: %r is %s' %
         (function_name, input, type(input)))
    if not len(input) > 0:
        raise ValueError('list for %s has zero len: %r' % (function_name, input))

def validate_result(result, function_name):
    """TODO: Ensure result is valid with iteration expense"""
    if not isinstance(result, int):
        raise TypeError('unsupported type in operand for %s: %r is %s' %
         (function_name, result, type(result)))