import datetime as dt
import pytz
from utils.validation import validate_operand, validate_result


def mean(dt_list):
    """TODO"""
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
    
    validate_result(mean_dt, "timestats.mean")
    return mean_dt


def median(dt_list):
    """TODO"""
    validate_operand(dt_list)
    sorted_dt_list = sorted(dt_list)
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

    validate_result(median, "timestats.median")
    return median_dt


nyc = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('America/New_York'))
london = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Europe/London'))
singapore = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Asia/Singapore'))
utc = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.utc)
naive_1 = dt.datetime(2015, 9, 10, 12, 0, 0)
naive_2 = dt.datetime(2015, 9, 30, 12, 0, 0)
naive_3 = dt.datetime(2015, 9, 22, 12, 0, 0)
naive_4 = dt.datetime(2015, 9, 12, 12, 0, 0)

n1 = [naive_1, naive_2, naive_3]


#print "london:    ", london
#print "nyc:       ", nyc
#print "singapore: ", singapore
#print "utc:       ", utc

t1 = [london, nyc, singapore, utc]
t2 = [london, nyc, singapore]
t3 = [london, nyc, london]
t4 = [london, nyc]

foo = [london, naive_1]

#print "naive 01:     ", naive_1
#print "naive 02:     ", naive_2
#print "naive 03:     ", naive_3
#print "naive 04:     ", naive_4

k = t1

print
for entry in k:
    print entry

print "\nMedian is: %s\nMean is:   %s\n" % (median(k), mean(k)) 

print "Is 1 valid?: %s" % valid(1)
print "Is 'a' valid?: %s" % valid('a')
print "Is t1 valid?: %s" % valid(t1)
print "Is n1 valid?: %s" % valid(n1)
print "Is foo valid?: %s" % valid(foo)


#print "\nBreak it 1: %s" % median(1)
#print "\nBreak it 1: %s" % median('a')