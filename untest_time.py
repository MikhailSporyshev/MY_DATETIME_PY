import unittest	
import datetime
from classes.my_time import my_time 

class TestTime(unittest.TestCase):
	MIN_MSEC = 0
	MIN_SEC = 0
	MIN_MIN = 0
	MIN_HOUR = 0
	MAX_MSEC = 999999
	MAX_SEC = 59
	MAX_MIN = 59
	MAX_HOUR = 23

	def test_init(self):
		time = my_time()
		self.assertEqual(time.msc, TestTime.MIN_MSEC)
		self.assertEqual(time.sc, TestTime.MIN_SEC)
		self.assertEqual(time.mn, TestTime.MIN_MIN)
		self.assertEqual(time.hr, TestTime.MIN_HOUR)

		for msc in [TestTime.MIN_MSEC,(TestTime.MIN_MSEC+TestTime.MAX_MSEC)//2,TestTime.MAX_MSEC]:
			for sc in [TestTime.MIN_SEC,(TestTime.MIN_SEC+TestTime.MAX_SEC)//2,TestTime.MAX_SEC]:
				for mn in [TestTime.MIN_MIN,(TestTime.MIN_MIN+TestTime.MAX_MIN)//2,TestTime.MAX_MIN]:
					for hr in [TestTime.MIN_HOUR,(TestTime.MIN_HOUR+TestTime.MAX_HOUR)//2,TestTime.MAX_HOUR]:
						time = my_time(msc,sc,mn,hr)
						self.assertEqual(time.msc, msc)
						self.assertEqual(time.sc, sc)
						self.assertEqual(time.mn, mn)
						self.assertEqual(time.hr, hr)

		with self.assertRaises(ValueError):
			time = my_time(TestTime.MIN_MSEC-1,TestTime.MIN_SEC,TestTime.MIN_MIN,TestTime.MIN_HOUR)
		with self.assertRaises(ValueError):
			time = my_time(TestTime.MIN_MSEC,TestTime.MIN_SEC-1,TestTime.MIN_MIN,TestTime.MIN_HOUR)
		with self.assertRaises(ValueError):
			time = my_time(TestTime.MIN_MSEC,TestTime.MIN_SEC,TestTime.MIN_MIN-1,TestTime.MIN_HOUR)
		with self.assertRaises(ValueError):
			time = my_time(TestTime.MIN_MSEC,TestTime.MIN_SEC,TestTime.MIN_MIN,TestTime.MIN_HOUR-1)


		with self.assertRaises(ValueError):
			time = my_time(TestTime.MIN_MSEC-10,TestTime.MIN_SEC,TestTime.MIN_MIN,TestTime.MIN_HOUR)
		with self.assertRaises(ValueError):
			time = my_time(TestTime.MIN_MSEC,TestTime.MIN_SEC-10,TestTime.MIN_MIN,TestTime.MIN_HOUR)
		with self.assertRaises(ValueError):
			time = my_time(TestTime.MIN_MSEC,TestTime.MIN_SEC,TestTime.MIN_MIN-10,TestTime.MIN_HOUR)
		with self.assertRaises(ValueError):
			time = my_time(TestTime.MIN_MSEC,TestTime.MIN_SEC,TestTime.MIN_MIN,TestTime.MIN_HOUR-10)

		with self.assertRaises(ValueError):
			time = my_time(TestTime.MAX_MSEC+1,TestTime.MAX_SEC,TestTime.MAX_MIN,TestTime.MAX_HOUR)
		with self.assertRaises(ValueError):
			time = my_time(TestTime.MAX_MSEC,TestTime.MAX_SEC+1,TestTime.MAX_MIN,TestTime.MAX_HOUR)
		with self.assertRaises(ValueError):
			time = my_time(TestTime.MAX_MSEC,TestTime.MAX_SEC,TestTime.MAX_MIN+1,TestTime.MAX_HOUR)
		with self.assertRaises(ValueError):
			time = my_time(TestTime.MAX_MSEC,TestTime.MAX_SEC,TestTime.MAX_MIN,TestTime.MAX_HOUR+1)


		with self.assertRaises(ValueError):
			time = my_time(TestTime.MAX_MSEC+10,TestTime.MAX_SEC,TestTime.MAX_MIN,TestTime.MAX_HOUR)
		with self.assertRaises(ValueError):
			time = my_time(TestTime.MAX_MSEC,TestTime.MAX_SEC+10,TestTime.MAX_MIN,TestTime.MAX_HOUR)
		with self.assertRaises(ValueError):
			time = my_time(TestTime.MAX_MSEC,TestTime.MAX_SEC,TestTime.MAX_MIN+10,TestTime.MAX_HOUR)
		with self.assertRaises(ValueError):
			time = my_time(TestTime.MAX_MSEC,TestTime.MAX_SEC,TestTime.MAX_MIN,TestTime.MAX_HOUR+10)
		

	def test_msec_valid(self):
		for msc in [TestTime.MIN_MSEC,(TestTime.MIN_MSEC+TestTime.MAX_MSEC)//2,TestTime.MAX_MSEC]:	
			self.assertTrue(my_time._is_msec_valid(msc))

		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_msec_valid(TestTime.MIN_MSEC-1))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_msec_valid(TestTime.MIN_MSEC-10))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_msec_valid(TestTime.MAX_MSEC+1))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_msec_valid(TestTime.MAX_MSEC+10))	

	def test_sec_valid(self):
		for sc in [TestTime.MIN_SEC,(TestTime.MIN_SEC+TestTime.MAX_SEC)//2,TestTime.MAX_SEC]:	
			self.assertTrue(my_time._is_sec_valid(sc))

		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_sec_valid(TestTime.MIN_SEC-1))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_sec_valid(TestTime.MIN_SEC-10))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_sec_valid(TestTime.MAX_SEC+1))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_sec_valid(TestTime.MAX_SEC+10))	

	def test_min_valid(self):
		for min in [TestTime.MIN_MIN,(TestTime.MIN_MIN+TestTime.MAX_MIN)//2,TestTime.MAX_MIN]:	
			self.assertTrue(my_time._is_min_valid(min))

		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_min_valid(TestTime.MIN_MIN-1))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_min_valid(TestTime.MIN_MIN-10))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_min_valid(TestTime.MAX_MIN+1))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_min_valid(TestTime.MAX_MIN+10))	
				
	def test_hour_valid(self):
		for hr in [TestTime.MIN_HOUR,(TestTime.MIN_HOUR+TestTime.MAX_HOUR)//2,TestTime.MAX_HOUR]:	
			self.assertTrue(my_time._is_hour_valid(hr))

		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_hour_valid(TestTime.MIN_HOUR-1))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_hour_valid(TestTime.MIN_HOUR-10))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_hour_valid(TestTime.MAX_HOUR+1))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_hour_valid(TestTime.MAX_HOUR+10))	
				
				
	
	def test_time_valid(self):		
		for msc in [TestTime.MIN_MSEC,(TestTime.MIN_MSEC+TestTime.MAX_MSEC)//2,TestTime.MAX_MSEC]:
			for sc in [TestTime.MIN_SEC,(TestTime.MIN_SEC+TestTime.MAX_SEC)//2,TestTime.MAX_SEC]:
				for mn in [TestTime.MIN_MIN,(TestTime.MIN_MIN+TestTime.MAX_MIN)//2,TestTime.MAX_MIN]:
					for hr in [TestTime.MIN_HOUR,(TestTime.MIN_HOUR+TestTime.MAX_HOUR)//2,TestTime.MAX_HOUR]:
						self.assertTrue(my_time._is_time_valid(msc,sc,mn,hr))

		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_time_valid(TestTime.MIN_MSEC-1,TestTime.MIN_SEC,TestTime.MIN_MIN,TestTime.MIN_HOUR))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_time_valid(TestTime.MIN_MSEC,TestTime.MIN_SEC-1,TestTime.MIN_MIN,TestTime.MIN_HOUR))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_time_valid(TestTime.MIN_MSEC,TestTime.MIN_SEC,TestTime.MIN_MIN-1,TestTime.MIN_HOUR))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_time_valid(TestTime.MIN_MSEC,TestTime.MIN_SEC,TestTime.MIN_MIN,TestTime.MIN_HOUR-1))


		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_time_valid(TestTime.MIN_MSEC-10,TestTime.MIN_SEC,TestTime.MIN_MIN,TestTime.MIN_HOUR))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_time_valid(TestTime.MIN_MSEC,TestTime.MIN_SEC-10,TestTime.MIN_MIN,TestTime.MIN_HOUR))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_time_valid(TestTime.MIN_MSEC,TestTime.MIN_SEC,TestTime.MIN_MIN-10,TestTime.MIN_HOUR))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_time_valid(TestTime.MIN_MSEC,TestTime.MIN_SEC,TestTime.MIN_MIN,TestTime.MIN_HOUR-10))

		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_time_valid(TestTime.MAX_MSEC+1,TestTime.MAX_SEC,TestTime.MAX_MIN,TestTime.MAX_HOUR))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_time_valid(TestTime.MAX_MSEC,TestTime.MAX_SEC+1,TestTime.MAX_MIN,TestTime.MAX_HOUR))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_time_valid(TestTime.MAX_MSEC,TestTime.MAX_SEC,TestTime.MAX_MIN+1,TestTime.MAX_HOUR))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_time_valid(TestTime.MAX_MSEC,TestTime.MAX_SEC,TestTime.MAX_MIN,TestTime.MAX_HOUR+1))


		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_time_valid(TestTime.MAX_MSEC+10,TestTime.MAX_SEC,TestTime.MAX_MIN,TestTime.MAX_HOUR))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_time_valid(TestTime.MAX_MSEC,TestTime.MAX_SEC+10,TestTime.MAX_MIN,TestTime.MAX_HOUR))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_time_valid(TestTime.MAX_MSEC,TestTime.MAX_SEC,TestTime.MAX_MIN+10,TestTime.MAX_HOUR))
		with self.assertRaises(ValueError):
			self.assertTrue(my_time._is_time_valid(TestTime.MAX_MSEC,TestTime.MAX_SEC,TestTime.MAX_MIN,TestTime.MAX_HOUR+10))
					

	def test_set_msec(self):
		time = my_time()
		for msc in [TestTime.MIN_MSEC,(TestTime.MIN_MSEC+TestTime.MAX_MSEC)//2,TestTime.MAX_MSEC]:
			time.set_msec(msc)
			self.assertEqual(time.msc,msc)

		with self.assertRaises(ValueError):
			time.set_msec(TestTime.MIN_MSEC-1)

		with self.assertRaises(ValueError):
			time.set_msec(TestTime.MIN_MSEC-10)

		with self.assertRaises(ValueError):
			time.set_msec(TestTime.MAX_MSEC+1)			
		
		with self.assertRaises(ValueError):
			time.set_msec(TestTime.MAX_MSEC+10)			


	def test_set_sec(self):
		time = my_time()
		for sc in [TestTime.MIN_SEC,(TestTime.MIN_SEC+TestTime.MAX_SEC)//2,TestTime.MAX_SEC]:
			time.set_sec(sc)
			self.assertEqual(time.sc,sc)

		with self.assertRaises(ValueError):
			time.set_sec(TestTime.MIN_SEC-1)

		with self.assertRaises(ValueError):
			time.set_sec(TestTime.MIN_SEC-10)

		with self.assertRaises(ValueError):
			time.set_sec(TestTime.MAX_SEC+1)			
		
		with self.assertRaises(ValueError):
			time.set_sec(TestTime.MAX_SEC+10)			


	def test_set_min(self):
		time = my_time()
		for mn in [TestTime.MIN_MIN,(TestTime.MIN_MIN+TestTime.MAX_MIN)//2,TestTime.MAX_MIN]:
			time.set_min(mn)
			self.assertEqual(time.mn,mn)

		with self.assertRaises(ValueError):
			time.set_min(TestTime.MIN_MIN-1)

		with self.assertRaises(ValueError):
			time.set_min(TestTime.MIN_MIN-10)

		with self.assertRaises(ValueError):
			time.set_min(TestTime.MAX_MIN+1)			
		
		with self.assertRaises(ValueError):
			time.set_min(TestTime.MAX_MIN+10)			


	def test_set_hour(self):
		time = my_time()
		for hr in [TestTime.MIN_HOUR,(TestTime.MIN_HOUR+TestTime.MAX_HOUR)//2,TestTime.MAX_HOUR]:
			time.set_hour(hr)
			self.assertEqual(time.hr,hr)

		with self.assertRaises(ValueError):
			time.set_hour(TestTime.MIN_HOUR-1)

		with self.assertRaises(ValueError):
			time.set_hour(TestTime.MIN_HOUR-10)

		with self.assertRaises(ValueError):
			time.set_hour(TestTime.MAX_HOUR+1)			
		
		with self.assertRaises(ValueError):
			time.set_hour(TestTime.MAX_HOUR+10)			



	def test_set_time(self):		
		time = my_time()		
		for msc in [TestTime.MIN_MSEC,(TestTime.MIN_MSEC+TestTime.MAX_MSEC)//2,TestTime.MAX_MSEC]:
			for sc in [TestTime.MIN_SEC,(TestTime.MIN_SEC+TestTime.MAX_SEC)//2,TestTime.MAX_SEC]:
				for mn in [TestTime.MIN_MIN,(TestTime.MIN_MIN+TestTime.MAX_MIN)//2,TestTime.MAX_MIN]:
					for hr in [TestTime.MIN_HOUR,(TestTime.MIN_HOUR+TestTime.MAX_HOUR)//2,TestTime.MAX_HOUR]:
						time.set_time(msc,sc,mn,hr)

		with self.assertRaises(ValueError):
			time.set_time(TestTime.MIN_MSEC-1,TestTime.MIN_SEC,TestTime.MIN_MIN,TestTime.MIN_HOUR)
		with self.assertRaises(ValueError):
			time.set_time(TestTime.MIN_MSEC,TestTime.MIN_SEC-1,TestTime.MIN_MIN,TestTime.MIN_HOUR)
		with self.assertRaises(ValueError):
			time.set_time(TestTime.MIN_MSEC,TestTime.MIN_SEC,TestTime.MIN_MIN-1,TestTime.MIN_HOUR)
		with self.assertRaises(ValueError):
			time.set_time(TestTime.MIN_MSEC,TestTime.MIN_SEC,TestTime.MIN_MIN,TestTime.MIN_HOUR-1)


		with self.assertRaises(ValueError):
			time.set_time(TestTime.MIN_MSEC-10,TestTime.MIN_SEC,TestTime.MIN_MIN,TestTime.MIN_HOUR)
		with self.assertRaises(ValueError):
			time.set_time(TestTime.MIN_MSEC,TestTime.MIN_SEC-10,TestTime.MIN_MIN,TestTime.MIN_HOUR)
		with self.assertRaises(ValueError):
			time.set_time(TestTime.MIN_MSEC,TestTime.MIN_SEC,TestTime.MIN_MIN-10,TestTime.MIN_HOUR)
		with self.assertRaises(ValueError):
			time.set_time(TestTime.MIN_MSEC,TestTime.MIN_SEC,TestTime.MIN_MIN,TestTime.MIN_HOUR-10)

		with self.assertRaises(ValueError):
			time.set_time(TestTime.MAX_MSEC+1,TestTime.MAX_SEC,TestTime.MAX_MIN,TestTime.MAX_HOUR)
		with self.assertRaises(ValueError):
			time.set_time(TestTime.MAX_MSEC,TestTime.MAX_SEC+1,TestTime.MAX_MIN,TestTime.MAX_HOUR)	
		with self.assertRaises(ValueError):
			time.set_time(TestTime.MAX_MSEC,TestTime.MAX_SEC,TestTime.MAX_MIN+1,TestTime.MAX_HOUR)
		with self.assertRaises(ValueError):
			time.set_time(TestTime.MAX_MSEC,TestTime.MAX_SEC,TestTime.MAX_MIN,TestTime.MAX_HOUR+1)


		with self.assertRaises(ValueError):
			time.set_time(TestTime.MAX_MSEC+10,TestTime.MAX_SEC,TestTime.MAX_MIN,TestTime.MAX_HOUR)
		with self.assertRaises(ValueError):
			time.set_time(TestTime.MAX_MSEC,TestTime.MAX_SEC+10,TestTime.MAX_MIN,TestTime.MAX_HOUR)
		with self.assertRaises(ValueError):
			time.set_time(TestTime.MAX_MSEC,TestTime.MAX_SEC,TestTime.MAX_MIN+10,TestTime.MAX_HOUR)
		with self.assertRaises(ValueError):
			time.set_time(TestTime.MAX_MSEC,TestTime.MAX_SEC,TestTime.MAX_MIN,TestTime.MAX_HOUR+10)
					
	
	def test_number_of_seconds(self):
		time = my_time()
		self.assertEqual(my_time._number_of_seconds(time),0)

		time.set_sec(1)
		self.assertEqual(my_time._number_of_seconds(time),1)			
		time.set_sec(0)

		time.set_min(1)
		self.assertEqual(my_time._number_of_seconds(time),60)			
		time.set_min(0)

		time.set_hour(1)
		self.assertEqual(my_time._number_of_seconds(time),3600)			
		time.set_hour(0)

	def test_difference(self):
		time1 = my_time()
		time2 = my_time(0,1,0,0)
		self.assertEqual(time1.difference(time2), -1)
		self.assertEqual(time2.difference(time1), 1)
			

if __name__ == '__main__':
	unittest.main()