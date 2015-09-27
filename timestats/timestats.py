import datetime as dt
import pytz
#from utils.validation import validate_operand, validate_result

def validate_operand(operand):
    """TODO"""
    if not isinstance(operand, list):
        raise TypeError('unsupported operand for timestat, requires list of datetime objects: %r is %s' %
         (operand, type(operand)))
    elif not len(operand) > 0:
        raise ValueError('must have non-zero len list for timestat, passed: %r' % operand)

def validate_result(answer_dt):
    """TODO docs + comment why conditional and not assertion and why never happen"""
    if not isinstance(answer_dt, dt.datetime):
        raise TypeError('non-datetime object in list: %r' % answer_dt)  
    if not answer_dt.tzinfo:
        return answer_dt
    else:
        return answer_dt.astimezone(pytz.utc)

def mean(dt_list):
    """
    TODO
    will raise TypeError if any item in list is not a datetime
    TODO if tz, convert to utc as part of validate answer
    """
    validate_operand(dt_list)
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
    return middlemost (not always UTC)
    TODO if tz, convert to utc as part of validate answer
    """
    validate_operand(dt_list)

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

# TESTS
# DTs  with TZ - show succeed, regardless of mixed TZs
nyc = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('America/New_York'))
london = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Europe/London'))
singapore = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Asia/Singapore'))
utc = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.utc)

t1 = [london, nyc, singapore, utc]
t2 = [london, nyc, singapore]
t3 = [london, nyc, london]
t4 = [london, nyc]

# Naive DTs - should succeed
naive_1 = dt.datetime(2015, 9, 10, 12, 0, 0)
naive_2 = dt.datetime(2015, 9, 30, 12, 0, 0)
naive_3 = dt.datetime(2015, 9, 22, 12, 0, 0)
naive_4 = dt.datetime(2015, 9, 12, 12, 0, 0)

n1 = [naive_1, naive_2, naive_3]

# Mixed DTs - should fail
foo = [london, naive_1]

# Non lists - all should fail
a_set = set([0])
an_int = 1
a_float = 2.0
a_str = "three"
a_tuple = (4, 5)

# Zero len list - should fail
z = []

# Mixed list
m1 = [london, an_int]

# RUN IT
"""
k = foo

if isinstance(k, list):
    print
    for entry in k:
        print entry

print "\nMean is: %s" % (mean(k)) 
print "Median is:   %s\n" % (median(k)) 
"""