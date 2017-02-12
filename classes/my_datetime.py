from my_date import my_date 
from my_time import my_time


class my_datetime:


	def __init__(self, msc = my_time._MIN_MSEC, sc = my_time._MIN_SEC, mn = my_time._MIN_MIN,\
	 hr = my_time._MIN_HOUR, day = my_date._MIN_DAY, month = my_date._MIN_MONTH, year = my_date._MIN_YEAR):#throws ValueError
		time = my_time(msc, sc, mn, hr);
		date = my_date(day, month, year);
