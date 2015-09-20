# Building blocks for testing

import datetime as dt
import pytz

nyc = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('America/New_York'))
london = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Europe/London'))
singapore = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Asia/Singapore'))
utc = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.utc)

print "nyc is ", nyc
print "london is ", london
print "utc is ", utc
print "singapore is ", singapore

print '\nPrinting Alpha'
alpha = [london, nyc, singapore, utc]

for i in alpha:
    print i

ordered = sorted(alpha)

print "\nPrinting Ordered"
for k in ordered:
    print k
