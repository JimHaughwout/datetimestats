datetimestats
=============
.. image:: https://travis-ci.org/JimHaughwout/datetimestats.svg?branch=master
    :target: https://travis-ci.org/JimHaughwout/datetimestats

Useful math stats functions for collections of datetime objects.

Ever had a list or set of datetimes and needed to perform some basic
statistical functions to find the median, mean, minimum, or maximum?
datetimestats provides some basic utilities to do this without the
overhead of converting to a numeric data type (e.g., unix timestamps at
millisecond-level) or pandas data frames (in order to employ pandas time
series functionality).

datetimestats takes any iterable of datetime objects (including panda
Series). It supports naive and non-naive datetimes, including iterables
of objects with different `Olson
timezones <https://en.wikipedia.org/wiki/Tz_database>`__. However, it
does not support iterables that contain both naive *and* non-naive
datetime objects.

Currently, datetimestats is supported for use with Python 2.7.

Installation
------------

Install using `pip <http://www.pip-installer.org/en/latest/>`__ with:

.. code:: sh

    pip install datetimestats

Or download a wheel or source archive from PyPI.

Usage
-----

datatimestats currently supports obtaining the the mean, median, min, or
max of an Iterable of datetime objects. The functions are designed to
minimize time complexity where possible.

Caluclating Means
~~~~~~~~~~~~~~~~~

Mean is calculated as the the arithmetic mean across datetime objects
with micro-second precision.

When given a list of naive datetimes, mean returns a naive datetime
object

.. code:: python

    >>> import datetime as dt
    >>> naive_1 = dt.datetime(2015, 9, 10, 12, 30, 0)
    >>> naive_2 = dt.datetime(2015, 9, 10, 12, 0, 0)
    >>> from datetimestats import mean
    >>> mean([naive_1, naive_2])
    datetime.datetime(2015, 9, 10, 12, 15)

When given a list of non-naive datetimes, it returns the mean as a
datetime object in ``UTC`` time:

.. code:: python

    >>> import datetime as dt
    >>> import pytz
    >>> nyc_noon = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('America/New_York'))
    >>> print nyc_noon # Curiosity of pytz, it does not convert to whole time zones
    2014-01-01 12:00:00-04:56
    >>> london_noon = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Europe/London'))
    >>> singapore_noon = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Asia/Singapore'))
    >>> from datetimestats import mean
    >>> mean([nyc_noon, london_noon, singapore_noon])
    datetime.datetime(2014, 1, 1, 11, 20, 40, tzinfo=<UTC>)

Calculating Medians
~~~~~~~~~~~~~~~~~~~

If an odd number of objects are provided, median is calculated is the
inner-most, sorted value. If an even number is provided, median is the
arithmetic-mean of the two inner-most, sorted values.

Odd number of values:

.. code:: python

    >>> import datetime as dt
    >>> import pytz
    >>> london_noon = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Europe/London'))
    >>> nyc_noon = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('America/New_York'))
    >>> singapore_noon = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Asia/Singapore'))
    >>> from datetimestats import median
    >>> median([nyc_noon, london_noon, singapore_noon])
    datetime.datetime(2014, 1, 1, 12, 0, tzinfo=<DstTzInfo 'Europe/London' LMT-1 day, 23:59:00 STD>)
    >>> median([nyc_noon, london_noon, singapore_noon]) == london_noon # Noon in London does fall between Singapore and NYC
    True

Even number of values:

.. code:: python

    >>> import datetime as dt
    >>> naive_1 = dt.datetime(2015, 9, 10, 12, 0, 0)
    >>> naive_2 = dt.datetime(2015, 9, 10, 14, 0, 0)
    >>> naive_3 = dt.datetime(2015, 9, 10, 13, 0, 0)
    >>> naive_4 = dt.datetime(2015, 9, 10, 15, 0, 0)
    >>> from datetimestats import median
    >>> median([naive_1, naive_2, naive_3, naive_4])
    datetime.datetime(2015, 9, 10, 14, 30)

Calculating Min and Max datetime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The min datetime is the *earliest* datetime. Conversely, the max is the
*latest*. This is most interesting when calculating across multiple
timezones:

.. code:: python

    >>> import datetime as dt
    >>> import pytz
    >>> london_noon = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Europe/London'))
    >>> nyc_noon = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('America/New_York'))
    >>> singapore_noon = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Asia/Singapore'))
    >>> from datetimestats import min, max
    >>> min([nyc_noon, london_noon, singapore_noon])
    datetime.datetime(2014, 1, 1, 12, 0, tzinfo=<DstTzInfo 'Asia/Singapore' LMT+6:55:00 STD>)
    >>> min([nyc_noon, london_noon, singapore_noon]) == singapore # It is noon in Singapore EARLIEST
    True
    >>> max([nyc_noon, london_noon, singapore_noon])
    datetime.datetime(2014, 1, 1, 12, 0, tzinfo=<DstTzInfo 'America/New_York' LMT-1 day, 19:04:00 STD>)
    >>> max([nyc_noon, london_noon, singapore_noon]) == nyc_noon # It is noon in NYC LATEST
    True

Others
~~~~~~

Sets, tuples, numpy Arrays and pandas Series are also supported:

.. code:: python

    >>> import datetime as dt
    >>> naive_1 = dt.datetime(2015, 9, 10, 12, 0, 0)
    >>> naive_2 = dt.datetime(2015, 9, 10, 14, 0, 0)
    >>> from datetimestats import median
    >>> median([naive_1, naive_2])
    datetime.datetime(2015, 9, 10, 13, 0)
    >>> median((naive_1, naive_2))
    datetime.datetime(2015, 9, 10, 13, 0)
    >>> import numpy as np
    >>> median(np.asarray([naive_1, naive_2]))
    datetime.datetime(2015, 9, 10, 13, 0)
    >>> import pandas as pd
    >>> median(pd.Series([naive_1, naive_2]))
    datetime.datetime(2015, 9, 10, 13, 0)
