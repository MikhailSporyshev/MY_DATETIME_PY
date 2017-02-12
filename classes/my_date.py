
class my_date:
#basic restrictions
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

	_DAYS_OF_WEEK = [6, 0, 1, 2, 3, 4, 5]

	@staticmethod
	def _is_year_leap(year):
		if  year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
			return True
		else:
			return False	

	@staticmethod		
	def _is_day_valid(day, month, year):#throws ValueError
		if my_date._is_year_valid(year):
			if my_date._is_month_valid(month):
				_MAX_DAY = my_date._DAYS_IN_MONTH[month]
				if my_date._is_year_leap(year):
					if month == 2:
						_MAX_DAY += 1

				if day >= my_date._MIN_DAY and day <= _MAX_DAY:
					return True
				else:
					#print("\"day invalid\"")
					raise ValueError
				

	@staticmethod
	def _is_month_valid(month):#throws ValueError
		if my_date._MIN_MONTH <= month <= my_date._MAX_MONTH:
			return True
		else:
			#print("\"month invalid\"")
			raise ValueError
		

	@staticmethod	
	def _is_year_valid(year):#throws ValueError
		if my_date._MIN_YEAR <= year <= my_date._MAX_YEAR:
			return True
		else:
			#print("\"year invalid\"")
			raise ValueError
		
		

	def __init__(self, day = _MIN_DAY, month = _MIN_MONTH, year = _MIN_YEAR):#throws ValueError
	#if any of the conditions is false the corrisponding error message will appear 	
		if my_date._is_day_valid(day, month,year):
		#all the conditions are true, the object of class date can be instanciated
			self.year = year
			self.day = day
			self.month = month


	def set_day(self, day):#throws ValueError
		if my_date._is_day_valid(day, self.month, self.year):
			self.day = day

	def set_month(self, month):#throws ValueError
		if my_date._is_month_valid(month):
			self.month = month

	def set_year(self, year):#throws ValueError
		if my_date._is_year_valid(year):
			self.year = year

	def set_date(self, day, month, year):#throws ValueError	
		if my_date._is_day_valid(day, month, year):
			self.year = year
			self.day = day
			self.month = month 

	@staticmethod	
	def _days_in_year(year):#throws ValueError	
		if my_date._is_year_valid(year):
			return 365 + my_date._is_year_leap(year)
			
	@staticmethod
	def _days_before_year(year):#throws ValueError	
		if my_date._is_year_valid(year):
			y = year - 1
			return y * 365 +  y//4 - y//100 + y//400	
			
	@staticmethod#
	def _days_in_month(month,year):#throws ValueError	
		if my_date._is_year_valid(year) and	my_date._is_month_valid(month):
				if month == 2 and my_date._is_year_leap(year):
					return 29 
				return my_date._DAYS_IN_MONTH[month]

	@staticmethod
	def _days_before_month(month,year):#throws ValueError	
		if my_date._is_year_valid(year) and my_date._is_month_valid(month):
				return my_date._DAYS_BEFORE_MONTH[month] + (month > 2 and my_date._is_year_leap(year))
				
	@staticmethod
	def _number_of_days(inst):
		return inst.day + my_date._days_before_month(inst.month,inst.year) + my_date._days_before_year(inst.year)		
	
#	@staticmethod
#	def _number_of_seconds(inst):
#		return my_date._number_of_days(inst) * 24 * 60 * 60	

#	def display_date(self):	
#		print(self.day, self.month, self.year)
 


	def difference(self, other):
		return my_date._number_of_days(self) - my_date._number_of_days(other)

	def day_of_week(self):
		return my_date._DAYS_OF_WEEK[my_date._number_of_days(self) % 7]	

