from my_date import my_date
from my_time import my_time
from my_timedelta import my_timedelta

class my_datetime:


	def __init__(self, msc = my_time._MIN_MSEC, sc = my_time._MIN_SEC, mn = my_time._MIN_MIN,\
	 hr = my_time._MIN_HOUR, day = my_date._MIN_DAY, month = my_date._MIN_MONTH, year = my_date._MIN_YEAR):#throws ValueError
		time = my_time(msc, sc, mn, hr);
		date = my_date(day, month, year);

    def __sub__(self, other):
        days = self.date._number_of_days() - other.date._number_of_days()    
        seconds = self.time._number_of_seconds() - other.time._number_of_seconds()
        if seconds < 0:
            days -= 1
            seconds += 3600 * 24

        return my_timedelta(days, seconds)

    def __lt__(self, other):#<
        return  self.date < other.date and self.time < other.time

    def __le__(self, other):#<=
        return self.date <= other.date and self.time <= other.time

    def __eq__(self, other):#=
        return self.date == other.date and self.time == other.time

    def __ne__(self, other):#!=
        return self.date != other.date and self.time != other.time

    def __gt__(self, other):#>
        return self.date > other.date and self.time > other.time

    def __ge__(self, other):#>=
        return self.date >= other.date and self.time >= other.time 