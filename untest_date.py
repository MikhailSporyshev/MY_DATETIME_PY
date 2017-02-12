import unittest	
import datetime
from classes.my_date import my_date 

class TestDate(unittest.TestCase):

	def test_default_init(self):
		somedate = my_date()
		self.assertEqual(somedate.day, my_date._MIN_DAY)
		self.assertEqual(somedate.month, my_date._MIN_MONTH)
		self.assertEqual(somedate.month, my_date._MIN_YEAR)

	def test_correct_init(self):
		day=1
		month=1
		year=1

		self.assertTrue(my_date._is_year_valid(year))
		self.assertTrue(my_date._is_month_valid(month))
		self.assertTrue(my_date._is_day_valid(day, month, year))

		somedate = my_date(day, month, year)
		
		self.assertEqual(somedate.day, day)
		self.assertEqual(somedate.month, month)
		self.assertEqual(somedate.month, year)

	def test_incorrect_init(self):
		with self.assertRaises(ValueError):
			 somedate = my_date(0,1,1)

		with self.assertRaises(ValueError):
			 somedate = my_date(1,0,1)
		
		with self.assertRaises(ValueError):
			 somedate = my_date(1,1,0)	 



	def test_year_valid(self):
		for year in range(my_date._MIN_YEAR,my_date._MAX_YEAR):
				self.assertTrue(my_date._is_year_valid(year))

		with self.assertRaises(ValueError):
			self.assertFalse(my_date._is_year_valid(0))	
		with self.assertRaises(ValueError):
			self.assertFalse(my_date._is_year_valid(-1))
		with self.assertRaises(ValueError):
			self.assertFalse(my_date._is_year_valid(10000))
		with self.assertRaises(ValueError):
			self.assertFalse(my_date._is_year_valid(10010))	
				

	def test_month_valid(self):
		for month in range(my_date._MIN_MONTH,my_date._MAX_MONTH):
				self.assertTrue(my_date._is_month_valid(month))
		
		with self.assertRaises(ValueError):
			self.assertFalse(my_date._is_month_valid(0))	
		with self.assertRaises(ValueError):
			self.assertFalse(my_date._is_month_valid(-1))
		with self.assertRaises(ValueError):
			self.assertFalse(my_date._is_month_valid(13))
		with self.assertRaises(ValueError):
			self.assertFalse(my_date._is_month_valid(20))	
		
		
	

	def test_day_valid(self):
		for year in [my_date._MIN_YEAR, 4, 100, 400,(my_date._MIN_YEAR + my_date._MAX_YEAR)//2, my_date._MAX_YEAR]:
			for month in [my_date._MIN_MONTH, 2, (my_date._MIN_MONTH + my_date._MAX_MONTH)//2, my_date._MAX_MONTH]: 
				
				_MAX_DAY=my_date._DAYS_IN_MONTH[month]
				if my_date._is_year_leap(year):
					if month==2:
						_MAX_DAY += 1

				self.assertTrue(my_date._is_day_valid(my_date._MIN_DAY, month, year))
				self.assertTrue(my_date._is_day_valid(14, month, year))
				self.assertTrue(my_date._is_day_valid(_MAX_DAY, month, year))
				
				with self.assertRaises(ValueError):
					self.assertFalse(my_date._is_day_valid(_MAX_DAY + 1, month, year))				
				with self.assertRaises(ValueError):
					self.assertFalse(my_date._is_day_valid(_MAX_DAY + 10, month, year))				
				with self.assertRaises(ValueError):
					self.assertFalse(my_date._is_day_valid(0, month, year))				
				with self.assertRaises(ValueError):
					self.assertFalse(my_date._is_day_valid(-10, month, year))				
	
		with self.assertRaises(ValueError):
			self.assertFalse(my_date._is_day_valid(1,1,1000000))
		with self.assertRaises(ValueError):
			self.assertFalse(my_date._is_day_valid(0,1,1))
		with self.assertRaises(ValueError):
			self.assertFalse(my_date._is_day_valid(1,0,1))
		with self.assertRaises(ValueError):
			self.assertFalse(my_date._is_day_valid(1,1,0))	
	
	def test_set_year(self):
		date = my_date()
		
		date.set_year(my_date._MIN_YEAR)
		self.assertEqual(date.year, my_date._MIN_YEAR)
		
		date.set_year(my_date._MAX_YEAR)
		self.assertEqual(date.year, my_date._MAX_YEAR)
		
		date.set_year((my_date._MIN_YEAR + my_date._MAX_YEAR)//2)
		self.assertEqual(date.year, (my_date._MIN_YEAR + my_date._MAX_YEAR)//2)

		with self.assertRaises(ValueError):
			date.set_year(my_date._MIN_YEAR - 1)

		with self.assertRaises(ValueError):
			date.set_year(my_date._MIN_YEAR - 100)	
		
		with self.assertRaises(ValueError):
			date.set_year(my_date._MAX_YEAR + 1)

		with self.assertRaises(ValueError):
			date.set_year(my_date._MAX_YEAR + 100)	



	def test_set_month(self):		
		date = my_date()

		date.set_month(my_date._MIN_MONTH)
		self.assertEqual(date.month, my_date._MIN_MONTH)
		
		date.set_month(my_date._MAX_MONTH)
		self.assertEqual(date.month, my_date._MAX_MONTH)
		
		date.set_month((my_date._MIN_MONTH + my_date._MAX_MONTH)//2)
		self.assertEqual(date.month, (my_date._MIN_MONTH + my_date._MAX_MONTH)//2)

		with self.assertRaises(ValueError):
			date.set_month(my_date._MIN_MONTH - 1)

		with self.assertRaises(ValueError):
			date.set_month(my_date._MIN_MONTH + 100)	

		with self.assertRaises(ValueError):
			date.set_month(my_date._MAX_MONTH + 1)

		with self.assertRaises(ValueError):
			date.set_month(my_date._MAX_MONTH - 100)	
					

	def test_set_day(self):
		date = my_date()
		for year in [my_date._MIN_YEAR, 4, 100, 400,(my_date._MIN_YEAR + my_date._MAX_YEAR)//2, my_date._MAX_YEAR]:
			date.set_year(year)
			for month in [my_date._MIN_MONTH,2, (my_date._MIN_MONTH + my_date._MAX_MONTH)//2, my_date._MAX_MONTH]:
				date.set_month(month)
				
				_MAX_DAY=my_date._DAYS_IN_MONTH[month]
				if my_date._is_year_leap(year):
					if month==2:
						_MAX_DAY += 1

				date.set_day(my_date._MIN_DAY)
				self.assertEqual(date.day, my_date._MIN_DAY)
				
				date.set_day(_MAX_DAY)
				self.assertEqual(date.day,_MAX_DAY)
				
				date.set_day((my_date._MIN_DAY + _MAX_DAY)//2)
				self.assertEqual(date.day, (my_date._MIN_DAY + _MAX_DAY)//2)

				with self.assertRaises(ValueError):
					date.set_day(my_date._MIN_DAY - 1)

				with self.assertRaises(ValueError):
					date.set_day(my_date._MIN_DAY + 100)	
				
				with self.assertRaises(ValueError):
					date.set_day(_MAX_DAY + 1)

				with self.assertRaises(ValueError):
					date.set_day(_MAX_DAY - 100)	
								


	def test_set_date(self):
		date = my_date()
		for year in [my_date._MIN_YEAR, 4, 100, 400,(my_date._MIN_YEAR + my_date._MAX_YEAR)//2, my_date._MAX_YEAR]:
			for month in [my_date._MIN_MONTH,2, (my_date._MIN_MONTH + my_date._MAX_MONTH)//2, my_date._MAX_MONTH]:
				
				_MAX_DAY=my_date._DAYS_IN_MONTH[month]
				if my_date._is_year_leap(year):
					if month==2:
						_MAX_DAY += 1

				date.set_date(my_date._MIN_DAY, month, year)
				self.assertEqual(date.day, my_date._MIN_DAY)
				self.assertEqual(date.month, month)
				self.assertEqual(date.year, year)

				date.set_date(_MAX_DAY, month, year)
				self.assertEqual(date.day,_MAX_DAY)
				self.assertEqual(date.month, month)
				self.assertEqual(date.year, year)

				date.set_date((my_date._MIN_DAY + _MAX_DAY)//2, month, year)
				self.assertEqual(date.day, (my_date._MIN_DAY + _MAX_DAY)//2)
				self.assertEqual(date.month, month)
				self.assertEqual(date.year, year)
	
				with self.assertRaises(ValueError):
					date.set_date(my_date._MIN_DAY - 1, month, year)

				with self.assertRaises(ValueError):
					date.set_date(my_date._MIN_DAY + 100, month, year)	

				with self.assertRaises(ValueError):
					date.set_date(_MAX_DAY + 1, month, year)

				with self.assertRaises(ValueError):
					date.set_date(_MAX_DAY - 100, month, year)	
					
		with self.assertRaises(ValueError):
			date.set_date(1, my_date._MIN_MONTH - 1, 1)

		with self.assertRaises(ValueError):
			date.set_date(1, my_date._MIN_MONTH + 100, 1)	
		
		with self.assertRaises(ValueError):
			date.set_date(1, my_date._MAX_MONTH + 1, 1)

		with self.assertRaises(ValueError):
			date.set_date(1, my_date._MAX_MONTH - 100, 1)	
					

		with self.assertRaises(ValueError):
			date.set_date(1, 1, my_date._MIN_YEAR - 1)

		with self.assertRaises(ValueError):
			date.set_date(1, 1, my_date._MIN_YEAR - 100)	
		
		with self.assertRaises(ValueError):
			date.set_date(1, 1, my_date._MAX_YEAR + 1)

		with self.assertRaises(ValueError):
			date.set_date(1, 1, my_date._MAX_YEAR + 100)	
	

	def test_day_of_week(self):
		date1 = my_date(1,1,1)
		date2 = datetime.date(1,1,1)
		for year in [my_date._MIN_YEAR, 4, 100, 400,(my_date._MIN_YEAR + my_date._MAX_YEAR)//2, my_date._MAX_YEAR]:
			for month in [my_date._MIN_MONTH,2, (my_date._MIN_MONTH + my_date._MAX_MONTH)//2, my_date._MAX_MONTH]:
				_MAX_DAY=my_date._DAYS_IN_MONTH[month]
				if my_date._is_year_leap(year):
					if month==2:
						_MAX_DAY += 1
				for day in [my_date._MIN_DAY,(my_date._MIN_DAY + _MAX_DAY)//2, _MAX_DAY]:
					date1.set_date(day, month, year)
					date2 = date2.replace(year,month,day)
					self.assertEqual(date1.day_of_week(), date2.weekday())						

	def test_difference(self):
		date1 = my_date(1,1,1)
		date2 = my_date(2,1,1)
		self.assertEqual(date1.difference(date2),-1)
		self.assertEqual(date2.difference(date1), 1)
		
	def test_days_before_year(self):
		self.assertEqual(my_date._days_before_year(1),0)
		self.assertEqual(my_date._days_before_year(2),365)
		with self.assertRaises(ValueError):
			my_date._days_before_year(0)

	def test_days_before_month(self):
		self.assertEqual(my_date._days_before_month(1,1),0)
		self.assertEqual(my_date._days_before_month(2,1),31)
		with self.assertRaises(ValueError):
			my_date._days_before_year(0)

	def test_days_in_year(self):
		for year in [my_date._MIN_YEAR, 4, 100, 400,(my_date._MIN_YEAR + my_date._MAX_YEAR)//2, my_date._MAX_YEAR]:		
			days = 365
			if my_date._is_year_leap(year):
				days=366	
			self.assertEqual(my_date._days_in_year(year), days)

	def test_days_in_month(self):		
		DAYS_IN_MONTH = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		for year in [my_date._MIN_YEAR, 4, 100, 400,(my_date._MIN_YEAR + my_date._MAX_YEAR)//2, my_date._MAX_YEAR]:
			for month in range(1,12):
				self.assertEqual(my_date._days_in_month(month, year),\
					DAYS_IN_MONTH[month]+(month == 2 and my_date._is_year_leap(year)))	


if __name__ == '__main__':
	unittest.main()