
class my_date:

	_MIN_YEAR = 1
	_MAX_YEAR = 9999
	_MIN_MONTH = 1
	_MAX_MONTH = 12
	_MIN_DAY = 1

	_DAYS_IN_MONTH = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	_DAYS_BEFORE_MONTH = [None]
	dbm = 0
	for dim in _DAYS_IN_MONTH[1:]:
	    _DAYS_BEFORE_MONTH.append(dbm)
	    dbm += dim
	del dbm, dim

	def _is_year_leap(year):
		if  year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
			return True
		else:
			return False	

	def _is_day_valid(day, month, year):
		_MAX_DAY = my_date._DAYS_IN_MONTH[month]
		if my_date._is_year_leap(year):
			if month == 2:
				_MAX_DAY += 1

		if day >= my_date._MIN_DAY and day <= _MAX_DAY:
			return True
		else:
			print("\"day invalid\"")
			raise ValueError
			return False

	def _is_month_valid(month):
		if my_date._MIN_MONTH <= month <= my_date._MAX_MONTH:
			return True
		else:
			print("\"month invalid\"")
			raise ValueError
			return False

		
	def _is_year_valid(year):
		if my_date._MIN_YEAR <= year <= my_date._MAX_YEAR:
			return True
		else:
			print("\"year invalid\"")
			raise ValueError
			return False
		

	def __init__(self, day = _MIN_DAY, month = _MIN_MONTH, year = _MIN_YEAR):
		if my_date._is_year_valid(year) and \
		my_date._is_month_valid(month) and \
		my_date._is_day_valid(day, month,year):
			self.year = year
			self.day = day
			self.month = month 

	def set_day(self, day):
		if my_date._is_day_valid(day):
			self.day = day


	def set_month(self, month):
		if my_date._is_month_valid(month):
			self.month = month

	def set_year(self, year):
		if my_date._is_year_valid(year):
			self.year = year

	def set_date(self, day, month, year):	
		if my_date._is_year_valid(year) and \
		my_date._is_month_valid(month) and \
		my_date._is_day_valid(day, month,year):
			self.year = year
			self.day = day
			self.month = month 

	def display(self):
		print(self.day,self.month, self.year)

	def _days_in_year(year):
		return 365 + my_date._is_year_leap(year)	

	def _days_before_year(year):
		y = year - 1
		return y * 365 +  y//4 - y//100 + y//400	

	def _days_in_month(month,year):
		if my_date._is_month_valid(month):
			if month == 2 and my_date._is_year_leap(year):
				return 29 
			return my_date._DAYS_IN_MONTH[month]

	def _days_before_month(month,year):
		if my_date._is_month_valid(month):
			return my_date._DAYS_BEFORE_MONTH[month] + (month > 2 and my_date._is_year_leap(year))

	def _number_of_days(inst):
		return inst.day + my_date._days_before_month(inst.month,inst.year) + my_date._days_before_year(inst.year)		

	def _number_of_seconds(inst):
		return my_date._number_of_days(inst) * 24 * 60 * 60	

	def difference(self, other):
		return my_date._number_of_days(self) - my_date._number_of_days(other)


date1 = my_date(1, 1, 1)
date1.display()	
print(my_date._number_of_days(date1))
print(my_date._number_of_seconds(date1))