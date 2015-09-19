import datetime as dt


def mean(dt_list):
    list_size = len(dt_list)

    if list_size == 1:
        mean_dt = dt_list[0]
    elif (list_size == 2) and (dt_list[0] == dt_list[1]):
        mean_dt = dt_list[0]
    else:
        base_dt = dt.datetime(1970, 1, 1)
        delta_total = 0
        for item in dt_list:
            delta_total += (item - base_dt).total_seconds()

        delta = delta_total / float(list_size)
        mean_dt = base_dt + dt.timedelta(seconds=delta)
    
    return mean_dt


def median(dt_list):
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

    return median_dt




now = dt.datetime.now()
x = dt.datetime(2014, 9, 1, 12, 0, 0)
y = dt.datetime(2015, 9, 30, 12, 0, 0)
z = dt.datetime(2015, 9, 16, 12, 00, 0)
a = dt.datetime(2015, 10, 15, 12, 0, 0)

dtl = [x, y, z, a]
dtl = [x, y, y, a]


print "List is:"
for i in dtl:
    print i

print "\nMedian is: %s\nMean is:   %s\n" % (median(dtl), mean(dtl)) 