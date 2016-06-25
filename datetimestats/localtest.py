from timestats import *

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