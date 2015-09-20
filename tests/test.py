# Building blocks for testing

import datetime as dt
import pytz

nyc = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('America/New_York'))
london = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Europe/London'))
singapore = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Asia/Singapore'))
utc = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.utc)
naive = dt.datetime(2014, 1, 1, 12, 0, 0)

print "london:    ", london
print "naive:     ", naive
print "nyc:       ", nyc
print "singapore: ", singapore
print "utc:       ", utc

print '\nPrinting Alpha'
will_fail = [london, naive, nyc, singapore, utc]
will_pass = [london, nyc, singapore, utc]


for i in will_pass:
    print i

ordered = sorted(will_pass)

print "\nPrinting Ordered"
for k in ordered:
    print k
