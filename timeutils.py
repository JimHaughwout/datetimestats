import datetime as dt
import pytz
#from utils.validation import validate_operand, validate_result

def validate_dt_list(operand, full_check=False):
    """
    Validates that an object is a actual list for timestats methods.

    Rest TODO
    """
    if not isinstance(operand, list):
        raise TypeError('unsupported operand for timestat, requires list of datetime objects: %r is %s' %
         (operand, type(operand)))
    elif not len(operand) > 0:
        raise ValueError('must have non-zero len list for timestat, passed: %r' % operand)


def normalize_dt(dt_object):
    """
    .. py:function:: normalize_dt(dt_object)

    Normalizes a datetime object. 

    If datetime is naive, just returns it. Otherwise converts it to UTC.

        :param datetime dt_object: datetime object to normalize
        :return: normalized datetime object
        :rtype: datetime.datetime
        :raises TypeError: if object is not of type datetime.datetime

    note::
        Included and enforced to avoid passive errors. 
        Included as a public method as convenience for users.
    """
    if not isinstance(dt_object, dt.datetime):
        raise TypeError('non-datetime object in list: %r' % dt_object)  
    elif not dt_object.tzinfo:
        return dt_object
    else:
        return dt_object.astimezone(pytz.utc)


def mean(dt_list):
    """
    TODO
    will raise TypeError if any item in list is not a datetime
    """
    validate_dt_list(dt_list)
    list_size = len(dt_list)

    if list_size == 1:
        mean_dt = dt_list[0]
    elif (list_size == 2) and (dt_list[0] == dt_list[1]):
        mean_dt = dt_list[0]
    else:
        if dt_list[0].tzinfo:
            base_dt = dt.datetime(1970, 1, 1, 0, 0, 0, tzinfo=pytz.utc)
        else:
            base_dt = dt.datetime(1970, 1, 1)
        delta_total = 0
        for item in dt_list:
            delta_total += (item - base_dt).total_seconds()

        delta = delta_total / float(list_size)
        mean_dt = base_dt + dt.timedelta(seconds=delta)
    
    return validate_result(mean_dt)


def median(dt_list):
    """
    TODO
    will raise TypeError if any item in list is not a datetime
    """
    validate_dt_list(dt_list)

    try:
        sorted_dt_list = sorted(dt_list)
    except TypeError:
        raise
    
    list_size = len(sorted_dt_list)

    if list_size == 1:
        median_dt = sorted_dt_list[0]
    elif list_size == 2:
        median_dt = mean(sorted_dt_list)
    elif list_size % 2:
        middle = list_size >> 1
        median_dt = sorted_dt_list[middle]
    else:
        upper = list_size >> 1
        lower = upper - 1
        middle = [sorted_dt_list[lower], sorted_dt_list[upper]]
        median_dt = mean(middle)

    #validate_result(median, "timestats.median")
    return validate_result(median_dt)

