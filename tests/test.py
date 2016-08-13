import unittest
import datetime as dt
import pytz
import datetimestats as dts

class DateTimeStatsTest(unittest.TestCase):

	# Testing datetimestate.mean

	def test_mean_naive_1(self):
		"""
		Tests that mean of a single-length list of a datetime should return itself
		"""
		naive_1 = dt.datetime(2015, 9, 10, 12, 0, 0)
		n1 = [naive_1]

		self.assertEquals(dts.mean(n1), naive_1)


	def test_mean_naive_2_same(self):
		"""
		Tests that mean short-circuit that list of two duplicates should just return
		returnthe first element. This is faster than averageing two identical items.
		"""
		naive_1 = dt.datetime(2015, 9, 10, 12, 0, 0)
		naive_2 = dt.datetime(2015, 9, 10, 12, 0, 0)
		n2 = [naive_1, naive_2]

		self.assertEquals(dts.mean(n2), naive_1)


	def test_mean_naive_2_diff(self):
		"""
		Tests that the mean of 2015-09-10 12:30:00.00 and 2015-09-10 12:00:00.00
		(both naive) is 2015-09-10 12:15:00.00. Also tests length==2 short-circuit.
		"""
		naive_1 = dt.datetime(2015, 9, 10, 12, 30, 0)
		naive_2 = dt.datetime(2015, 9, 10, 12, 0, 0)
		n2 = [naive_1, naive_2]

		self.assertEquals(dts.mean(n2), dt.datetime(2015, 9, 10, 12, 15, 0))


	def test_mean_naive_3(self):
		"""
		Tests that the mean of 2015-09-10 12:00:00.00, 2015-09-30 12:00:00.00,
		and 2015-09-22 12:00.00.000 (all naive) is 2015-09-21 04:00:00.00
		"""
		naive_1 = dt.datetime(2015, 9, 10, 12, 0, 0)
		naive_2 = dt.datetime(2015, 9, 30, 12, 0, 0)
		naive_3 = dt.datetime(2015, 9, 22, 12, 0, 0)
		n3 = [naive_1, naive_2, naive_3]

		self.assertEquals(dts.mean(n3), dt.datetime(2015, 9, 21, 4, 0, 0))


	def test_mean_tz_1(self):
		"""
		Tests that mean of a single-length list of 1 datetime with timezone should return itself
		"""
		noon_zulu = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.utc)
		t1 = [noon_zulu]

		self.assertEquals(dts.mean(t1), noon_zulu)


	def test_mean_tz_2_same(self):
		"""
		Tests short-circuit that mean list of two duplicates should just return
		the first element. This is faster than averageing two identical items.
		"""
		noon_zulu = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.utc)
		noon_zulu_ditto = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.utc)
		t2 = [noon_zulu, noon_zulu_ditto]

		self.assertEquals(dts.mean(t2), noon_zulu)


	def test_mean_same_tz_2_diff_vals(self):
		"""
		Tests that mean of 1200 UTC and 1300 UTC is 1230 UTC.
		"""
		z_1200 = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.utc)
		z_1300 = dt.datetime(2014, 1, 1, 13, 0, 0, tzinfo=pytz.utc)
		t2 = [z_1300, z_1200]

		self.assertEquals(dts.mean(t2), dt.datetime(2014, 1, 1, 12, 30, 0, tzinfo=pytz.utc))


	def test_mean_same_tz_3_vals(self):
		"""
		Tests that mean of 1200 UTC, 1300 UTC, and 1315 UTC is 1245 UTC.
		"""
		z_1200 = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.utc)
		z_1300 = dt.datetime(2014, 1, 1, 13, 0, 0, tzinfo=pytz.utc)
		z_1315 = dt.datetime(2014, 1, 1, 13, 15, 0, tzinfo=pytz.utc)
		t3 = [z_1300, z_1315, z_1200]

		self.assertEquals(dts.mean(t3), dt.datetime(2014, 1, 1, 12, 45, 0, tzinfo=pytz.utc))


	def test_mean_diff_tz_2_vals(self):
		"""
		Tests mean of two values (short-circuit) across different timezones.
		Note: PYTZ does not cast timezones exactly to hours.
		      Try yourself (see the README)
		      mean of (2014-01-01 12:00:00-04:56, 2014-01-01 12:00:00-00:01) 
		      	is actually 2014-01-01 14:28:30+00:00
		"""
		nyc = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('America/New_York'))
		london = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Europe/London'))
		t2 = [nyc, london]

		self.assertEquals(dts.mean(t2), dt.datetime(2014, 1, 1, 14, 28, 30, tzinfo=pytz.utc))


	def test_mean_diff_tz_3_vals(self):
		"""
		Tests mean of three values across different timezones.
		Note: PYTZ does not cast timezones exactly to hours.
		      Try yourself (see the README)
		      mean of (2014-01-01 12:00:00-04:56, 2014-01-01 12:00:00-00:01, 2014-01-01 12:00:00+06:55) 
		      	is actually 2014-01-01 11:20:40+00:00
		"""
		nyc = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('America/New_York'))
		london = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Europe/London'))
		singapore = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Asia/Singapore'))
		t3 = [nyc, london, singapore]

		self.assertEquals(dts.mean(t3), dt.datetime(2014, 1, 1, 11, 20, 40, tzinfo=pytz.utc))


	def test_mean_diff_tz_4_vals(self):
		"""
		Tests mean for four values (not short-circuit) across multiple timezones.
		Note: PYTZ does not cast timezones exactly to hours.
		      Try yourself (see the README)
		"""

		chicago = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('America/Chicago'))
		nyc = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('America/New_York'))
		london = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Europe/London'))
		singapore = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Asia/Singapore'))
		t4 = [chicago, nyc, london, singapore]

		self.assertEquals(dts.mean(t4), dt.datetime(2014, 1, 1, 12, 58, 15, tzinfo=pytz.utc))


	def test_mean_empty(self):
		"""
		Tests return of IndexError when passing a zero-length list
		"""
		n1 = list()

		with self.assertRaises(IndexError):
			dts.mean(n1)


	def test_mean_invalid_operant_object(self):
		"""
		Tests return of a TypeError if passing non-datetime.datetime objects
		"""
		x1 = ['not a datetime.datetime']

		with self.assertRaises(TypeError):
			dts.mean(x1)


	def test_mean_operand_not_iterable(self):
		"""
		Tests return of a TypeError if passing non-datetime.datetime objects
		"""
		x1 = 1

		with self.assertRaises(TypeError):
			dts.mean(x1)


	# Testing datetimestate.median

	def test_median_naive_1(self):
		"""
		Tests that a single-length list of a datetime should return itself
		"""
		naive_1 = dt.datetime(2015, 9, 10, 12, 0, 0)
		n1 = [naive_1]

		self.assertEquals(dts.median(n1), naive_1)


	def test_median_naive_2_same(self):
		"""
		Tests short-circuit that list of twp duplicates should just return
		the first element. Faster than sorting and averaging two identical items.
		"""
		naive_1 = dt.datetime(2015, 9, 10, 12, 0, 0)
		naive_2 = dt.datetime(2015, 9, 10, 12, 0, 0)
		n2 = [naive_1, naive_2]

		self.assertEquals(dts.median(n2), naive_1)


	def test_median_naive_3(self):
		"""
		Tests that the median of 2015-09-10 12:00:00.00, 2015-09-30 12:00:00.00,
		and 2015-09-22 12:00.00.000 (all naive) is 2015-09-22 12:00.00.000.
		This is the middle value
		"""
		naive_1 = dt.datetime(2015, 9, 10, 12, 0, 0)
		naive_2 = dt.datetime(2015, 9, 30, 12, 0, 0)
		naive_3 = dt.datetime(2015, 9, 22, 12, 0, 0)
		n3 = [naive_1, naive_2, naive_3]

		self.assertEquals(dts.median(n3), naive_3)


	def test_median_naive_4_diff(self):
		"""
		Tests that the median of 2015-09-10 12:30:00.00 and 2015-09-10 12:00:00.00
		(both naive) is 2015-09-10 12:15:00.00 (arithmetic mean of middle two. 
		Also tests length==2 condition as this is a sub-set of this test.
		"""
		naive_1 = dt.datetime(2015, 9, 10, 12, 30, 0)
		naive_2 = dt.datetime(2015, 9, 10, 12, 0, 0)
		naive_3 = dt.datetime(2014, 9, 10, 12, 30, 0)
		naive_4 = dt.datetime(2016, 9, 10, 12, 30, 0)
		n4 = [naive_1, naive_2, naive_3, naive_4]

		self.assertEquals(dts.median(n4), dts.mean([naive_1, naive_2]))


	def test_median_tz_1(self):
		"""
		Tests that a single-length list of a datetime with timezone should return itself
		"""
		noon_zulu = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.utc)
		t1 = [noon_zulu]

		self.assertEquals(dts.median(t1), noon_zulu)


	def test_median_tz_2_same(self):
		"""
		Tests short-circuit that list of twp duplicates should just return
		the first element. This is faster than sorting and averaging two identical items.
		"""
		noon_zulu = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.utc)
		noon_zulu_ditto = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.utc)
		t2 = [noon_zulu, noon_zulu_ditto]

		self.assertEquals(dts.median(t2), noon_zulu)


	def test_median_same_tz_3_vals(self):
		"""
		Tests that median of 1200 UTC, 1300 UTC, and 1315 UTC is 1300 UTC.
		"""
		z_1200 = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.utc)
		z_1300 = dt.datetime(2014, 1, 1, 13, 0, 0, tzinfo=pytz.utc)
		z_1315 = dt.datetime(2014, 1, 1, 13, 15, 0, tzinfo=pytz.utc)
		t3 = [z_1300, z_1315, z_1200]

		self.assertEquals(dts.median(t3), dt.datetime(2014, 1, 1, 13, 0, 0, tzinfo=pytz.utc))


	def test_median_diff_tz_3_vals(self):
		"""
		Tests median for three values across different timezones.
		Note: This bypasses the PYTZ non-full unit issue as it just sorts the 
		odd number of timezones and returns the middle (London)
		"""
		nyc = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('America/New_York'))
		london = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Europe/London'))
		singapore = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Asia/Singapore'))
		t3 = [nyc, london, singapore]

		self.assertEquals(dts.median(t3), london)


	def test_median_diff_tz_4_vals(self):
		"""
		Tests median for four values across different timezones.
		Note: This sorts than computes the arithmetic mean of the middle two values.
			  As mentioned above, pytz does not always case to full timezone offsets
		"""
		chicago = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('America/Chicago'))
		nyc = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('America/New_York'))
		london = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Europe/London'))
		singapore = dt.datetime(2014, 1, 1, 12, 0, 0, tzinfo=pytz.timezone('Asia/Singapore'))
		t4 = [chicago, nyc, london, singapore]

		self.assertEquals(dts.median(t4), dts.mean([nyc, london]))


	def test_median_empty(self):
		"""
		Tests return of IndexError when passing a zero-length list
		"""
		n1 = list()

		with self.assertRaises(IndexError):
			dts.median(n1)


	def test_median_invalid_operant_object(self):
		"""
		Tests return of a TypeError if passing non-datetime.datetime objects
		"""
		x1 = ['not a datetime.datetime']

		with self.assertRaises(TypeError):
			dts.median(x1)


	def test_median_operand_not_iterable(self):
		"""
		Tests return of a TypeError if passing non-datetime.datetime objects
		"""
		x1 = 1

		with self.assertRaises(TypeError):
			dts.median(x1)