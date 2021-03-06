import datetime as dt
import pytz

_OPER_ERR_MSG = """unsupported operand.
datetimestat requires Iterable of datetime objects (all naive or all with tz). You passed:
"""
_LEN_ERR_MSG = """zero-length operand
datetimestat requires Iterable of length greater than zero. You passed an empty iterable.
"""
_VAL_ERR_MSG = """unsupported value.
datetimestat requires Iterable of datetime objects. Iterable contained:
"""

def validate_dt(candidate):
    """
    .. py:function:: validate_dt(candidate)

    If candidate is a datetime object, return it. Otherwise raise a TypeError.

        :param object candidate: object to validate
        :return: candidate (if validated)
        :rtype: datetime.datetime
        :raises TypeError: if object is not of type datetime.datetime
    """
    if not isinstance(candidate, dt.datetime):
        raise TypeError(_VAL_ERR_MSG + str(candidate))  
    else:
        return candidate


def mean(dt_list):
    """
    .. py:function:: mean(dt_list)

    Returns the mean datetime from an Iterable collection of datetime objects.
    Collection can be all naive datetime objects or all datatime objects with tz
    (if non-naive datetimes are provided, result will be cast to UTC).
    However, collection cannot be a mix of naive and non-naive datetimes.

    Can handle micro-second level datetime differences. Can handle Collection of 
    datetime objects with different timezones. Works with lists or pandas.Series.

        :param collection.Iterable dt_list: Iterable list or Series of datetime objects
        :return: mean datetime
        :rtype: datetime.datetime
        :raises TypeError: if operand is not type Iterable or 
                           if operand contains naive and non-naive datetime objects or
                           if result is not type datetime.datetime
    """
    try:
        list_size = len(dt_list)
    except TypeError:
        raise TypeError(_OPER_ERR_MSG + str(dt_list))

    if list_size == 1:
        mean_dt = dt_list[0]
    elif (list_size == 2) and (dt_list[0] == dt_list[1]):
        mean_dt = dt_list[0]
    else:
        try:
            if dt_list[0].tzinfo:
                base_dt = dt.datetime(1970, 1, 1, 0, 0, 0, tzinfo=pytz.utc)
            else:
                base_dt = dt.datetime(1970, 1, 1)
            delta_total = 0
            for item in dt_list:
                delta_total += (item - base_dt).total_seconds()

            delta = delta_total / float(list_size)
            mean_dt = base_dt + dt.timedelta(seconds=delta)
        except TypeError:
            raise TypeError(_OPER_ERR_MSG + str(dt_list))
        except IndexError:
            raise IndexError(_LEN_ERR_MSG)

    return validate_dt(mean_dt)


def median(dt_list):
    """
    .. py:function:: median(dt_list)

    Returns the median datetime from an Iterable collection of datetime objects.
    Collection can be all naive datetime objects or all datatime objects with tz.
    If non-naive datetimes are provided and list size is odd, result will be 
    middle-most datetime (with whatever time zone is provided). If list size is 
    even, result will be datetimestats.mean of two middle-most values (in UTC).
    However, collection cannot be a mix of naive and non-naive datetimes.

    Includes short-circuiting steps to speed computations on small collections.
    If Collection has even number of elements it will return the mean of inner
    two middle values.

    Can handle micro-second level datetime differences. Can handle Collection of 
    datetime objects with different timezones. Works with lists or pandas.Series.

        :param collection.Iterable dt_list: Iterable list or Series of datetime objects
        :return: median datetime
        :rtype: datetime.datetime
        :raises TypeError: if operand is not type Iterable or 
                           if operand contains naive and non-naive datetime objects or
                           if result is not type datetime.datetime
    """
    try:
        sorted_dt_list = sorted(dt_list)
        list_size = len(sorted_dt_list)
    except TypeError:
        raise TypeError(_OPER_ERR_MSG + str(dt_list))

    if list_size == 0:
        raise IndexError(_LEN_ERR_MSG)
    elif list_size == 1:
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

    return validate_dt(median_dt)


def min(dt_list):
    """
    .. py:function:: min(dt_list)

    Returns the earliest datetime from an Iterable collection of datetime objects.
    Collection can be all naive datetime objects or all datatime objects with tz.
    However, collection cannot be a mix of naive and non-naive datetimes.

    Can handle micro-second level datetime differences. Can handle Collection of 
    datetime objects with different timezones. Works with lists or pandas.Series.

        :param collection.Iterable dt_list: Iterable list or Series of datetime objects
        :return: min datetime
        :rtype: datetime.datetime
        :raises TypeError: if operand is not type Iterable or 
                           if operand contains naive and non-naive datetime objects or
                           if result is not type datetime.datetime
    """
    try:
        sorted_dt_list = sorted(dt_list)
        return validate_dt(sorted_dt_list[0])
    except TypeError:
        raise TypeError(_OPER_ERR_MSG + str(dt_list))


def max(dt_list):
    """
    .. py:function:: max(dt_list)

    Returns the latest datetime from an Iterable collection of datetime objects.
    Collection can be all naive datetime objects or all datatime objects with tz.
    However, collection cannot be a mix of naive and non-naive datetimes.

    Can handle micro-second level datetime differences. Can handle Collection of 
    datetime objects with different timezones. Works with lists or pandas.Series.

        :param collection.Iterable dt_list: Iterable list or Series of datetime objects
        :return: min datetime
        :rtype: datetime.datetime
        :raises TypeError: if operand is not type Iterable or 
                           if operand contains naive and non-naive datetime objects or
                           if result is not type datetime.datetime
    """
    try:
        sorted_dt_list = sorted(dt_list)
        return validate_dt(sorted_dt_list[-1])
    except TypeError:
        raise TypeError(_OPER_ERR_MSG + str(dt_list))