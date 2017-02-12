class my_time:
#basic restrictions
	_MIN_MSEC = 0
	_MIN_SEC = 0
	_MIN_MIN = 0
	_MIN_HOUR = 0
	_MAX_MSEC = 999999
	_MAX_SEC = 59
	_MAX_MIN = 59
	_MAX_HOUR = 23

	@staticmethod
	def _is_msec_valid(msc):
		if my_time._MIN_MSEC <= msc <= my_time._MAX_MSEC:
			return True
		else: 
			raise ValueError

	@staticmethod
	def _is_sec_valid(sc):
		if my_time._MIN_SEC <= sc <= my_time._MAX_SEC:
			return True
		else:
			raise ValueError


	@staticmethod
	def _is_min_valid(mn):
		if my_time._MIN_MIN <= mn <= my_time._MAX_MIN:
			return True
		else:
			raise ValueError				

	@staticmethod
	def _is_hour_valid(hr):
		if my_time._MIN_HOUR <= hr <= my_time._MAX_HOUR:
			return True
		else:
			raise ValueError		

	@staticmethod
	def _is_time_valid(msc, sc, mn, hr):
			if my_time._is_msec_valid(msc) and \
				my_time._is_sec_valid(sc) and \
				my_time._is_min_valid(mn) and \
				my_time._is_hour_valid(hr):
					return True
		


	def __init__(self, msc = _MIN_MSEC, sc = _MIN_SEC, mn = _MIN_MIN, hr = _MIN_HOUR):#throws ValueError
	#if any of the conditions is false the corrisponding error message will appear 	
		if my_time._is_time_valid(msc,sc,mn,hr):
		#all the conditions are true, the object of class date can be instanciated
			self.hr = hr
			self.mn = mn
			self.sc = sc
			self.msc = msc

	def set_msec(self, msc):#throws ValueError
		if my_time._is_msec_valid(msc):
			self.msc = msc

	def set_sec(self, sc):#throws ValueError
		if my_time._is_sec_valid(sc):
			self.sc = sc

	def set_min(self, mn):#throws ValueError
		if my_time._is_min_valid(mn):
			self.mn = mn

	def set_hour(self, hr):#throws ValueError
		if my_time._is_hour_valid(hr):
			self.hr = hr

	def set_time(self, msc, sc, mn, hr):#throws ValueError	
		if my_time._is_time_valid(msc, sc, mn, hr):
		#all the conditions are true, the object of class date can be instanciated
			self.hr = hr
			self.mn = mn
			self.sc = sc
			self.msc = msc 

#	def display_time(self):
#		print(self.msc, self.sc, self.mn, self.hr)

	@staticmethod
	def _number_of_seconds(inst):
		return inst.sc + inst.mn * 60 + inst.hr * 3600	
		
	def difference(self, other):
		return my_time._number_of_seconds(self) - my_time._number_of_seconds(other)

