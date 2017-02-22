import itertools

class my_date:
#basic restrictions
	_MIN_YEAR = 1
	_MAX_YEAR = 9999
	_MIN_MONTH = 1
	_MAX_MONTH = 12
	_MIN_DAY = 1

	_DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	_DAYS_BEFORE_MONTH = list(itertools.accumulate(_DAYS_IN_MONTH))
	_DAYS_BEFORE_MONTH.insert(0,0)

	_DAYS_OF_WEEK = [6, 0, 1, 2, 3, 4, 5]

	def __init__(self, day = _MIN_DAY, month = _MIN_MONTH, year = _MIN_YEAR):#throws ValueError
	#if any of the conditions is false the corrisponding error message will appear 	
		if my_date._is_day_valid(day, month,year):
		#all the conditions are true, the object of class date can be instanciated
			self.year = year
			self.day = day
			self.month = month
		else:
			raise ValueError	

	def set_day(self, day):#throws ValueError
		if my_date._is_day_valid(day, self.month, self.year):
			self.day = day
		else:
			raise ValueError	

	def set_month(self, month):#throws ValueError
		if my_date._is_month_valid(month):
			self.month = month
		else:
			raise ValueError	

	def set_year(self, year):#throws ValueError
		if my_date._is_year_valid(year):
			self.year = year
		else:
			raise ValueError

	def set_date(self, day, month, year):#throws ValueError	
		if my_date._is_day_valid(day, month, year):
			self.year = year
			self.day = day
			self.month = month
		else:
			raise ValueError 

	def get_day(self):
		return self.day

	def get_month(self):
		return self.month

	def get_year(self):
		return self.year
		
	def add_days(self, input_days):
		days_in_full_cycle = 400*365+400//4-400//100+400//400
		days_in_quarter_cycle = 100*365+100//4-100//100
		days_in_small_cycle = 365*4+4//4

		total_days = input_days + self._number_of_days()
		total_years=0

		full_cycle_count=total_days//days_in_full_cycle
		if full_cycle_count>0:
			total_days-=full_cycle_count*days_in_full_cycle
			total_years+=full_cycle_count*400

		quarter_cycle_count=input_days//days_in_quarter_cycle
		if quarter_cycle_count>0:
			total_days-=quarter_cycle_count*days_in_quarter_cycle
			total_years+=quarter_cycle_count*100

		small_cycle_count=total_days//days_in_small_cycle
		if small_cycle_count>0:
			total_days-=small_cycle_count*days_in_small_cycle
			total_years+=small_cycle_count*4

		years_count=total_days//365
		if years_count>0:
			total_days-=years_count*365
			total_years+=years_count

		if my_date._is_year_valid(total_years):
			total_month=0
			i = 0
			while my_date._days_before_month[i]+(i==2 and my_date._is_year_leap(total_years))<total_days:
				i += 1
			total_days-=my_date._days_before_month[i-1]
			total_month=[i-1]
			self.set_date(total_days,total_month,total_years)
		else:
			raise ValueError	

	def add_months(self, input_months):
		if my_date._is_month_valid(self.month + input_months):
			self.set_month(self.month+input_months)
		else:
			raise ValueError	
		
	def add_years(self, input_years):
		if my_date._is_year_valid(self.year + input_years):
			self.set_year(self.year+input_years)
		else:
			raise ValueError

	def difference(self, other):
		return my_date._number_of_days(self) - my_date._number_of_days(other)

	def day_of_week(self):
		return my_date._DAYS_OF_WEEK[my_date._number_of_days(self) % 7]	

    def __lt__(self, other):#<
        return self.year<other.year or \
        	(self.year=other.year and self.month < other.month) or\
        	(self.year=other.year and self.month = other.month and self.day < other.day)
        	 

    def __le__(self, other):#<=
	    return self.year<other.year or \
        	(self.year=other.year and self.month < other.month) or\
        	(self.year=other.year and self.month = other.month and self.day <= other.day)
   

    def __eq__(self, other):#=
        return 

    def __ne__(self, other):#!=
        return 

    def __gt__(self, other):#>
        return 

    def __ge__(self, other):#>=
        return 	



	@staticmethod
	def _is_year_leap(year):
		return  year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

	@staticmethod		
	def _is_day_valid(day, month, year):
		if my_date._is_year_valid(year) and \
		my_date._is_month_valid(month):
			_MAX_DAY = my_date._DAYS_IN_MONTH[month]
			if my_date._is_year_leap(year) and month == 2:
				_MAX_DAY += 1

			if day >= my_date._MIN_DAY and day <= _MAX_DAY:
				return True
		return False
				
	@staticmethod
	def _is_month_valid(month):
		if my_date._MIN_MONTH <= month <= my_date._MAX_MONTH:
			return True
		else:
			return False
		
	@staticmethod	
	def _is_year_valid(year):
		if my_date._MIN_YEAR <= year <= my_date._MAX_YEAR:
			return True
		else:
			return False
		
	@staticmethod	
	def _days_in_year(year):
		if my_date._is_year_valid(year):
			return 365 + my_date._is_year_leap(year)
		else:
			raise ValueError	
			
	@staticmethod
	def _days_before_year(year):
		if my_date._is_year_valid(year):
			y = year - 1
			return y * 365 +  y//4 - y//100 + y//400
		else:
			raise ValueError		
			
	@staticmethod#
	def _days_in_month(month,year):
		if my_date._is_year_valid(year) and	my_date._is_month_valid(month):
				if month == 2 and my_date._is_year_leap(year):
					return 29 
				return my_date._DAYS_IN_MONTH[month]
		else:
			raise ValueError		

	@staticmethod
	def _days_before_month(month,year):#throws ValueError	
		if my_date._is_year_valid(year) and my_date._is_month_valid(month):
				return my_date._DAYS_BEFORE_MONTH[month] + (month > 2 and my_date._is_year_leap(year))
		else:
			raise ValueError		
				
	@staticmethod
	def _number_of_days(inst):
		return inst.day + my_date._days_before_month(inst.month,inst.year) + my_date._days_before_year(inst.year)		
