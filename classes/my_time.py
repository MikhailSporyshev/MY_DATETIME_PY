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

	def __init__(self, microseconds = _MIN_MSEC, seconds = _MIN_SEC, \
		minutes = _MIN_MIN, hours = _MIN_HOUR):
	#if any of the conditions is false the corrisponding error message will appear 	
		if my_time._is_time_valid(microseconds,seconds,minutes,hours):
		#all the conditions are true, the object of class date can be instanciated
			self.hours = hours
			self.minutes = minutes
			self.seconds = seconds
			self.microseconds = microseconds
		else:
			raise ValueError	

	def set_msec(self, microseconds):
		if my_time._is_msec_valid(microseconds):
			self.microseconds = microseconds
		else:
			raise ValueError

	def set_sec(self, seconds):
		if my_time._is_sec_valid(seconds):
			self.seconds = seconds
		else:
			raise ValueError

	def set_min(self, minutes):
		if my_time._is_min_valid(minutes):
			self.minutes = minutes
		else:
			raise ValueError
	
	def set_hour(self, hours):
		if my_time._is_hour_valid(hours):
			self.hours = hours
		else:
			raise ValueError

	def set_time(self, microseconds, seconds, minutes, hours):	
		if my_time._is_time_valid(microseconds, seconds, minutes, hours):
		#all the conditions are true, the object of class date can be instanciated
			self.hours = hours
			self.minutes = minutes
			self.seconds = seconds
			self.microseconds = microseconds 
		else:
			raise ValueError

	def get_msec(self):
		return self.microseconds

	def get_sec(self):
		return self.seconds

	def get_minutes(self):
		return self.minutes
	
	def get_hours(self):
		return self.hours					

	def add_msec(self, microseconds):
		if my_time._is_msec_valid(self.microseconds + microseconds):
			self.microseconds += microseconds
		else:
			raise ValueError

	def add_sec(self, seconds):
		if my_time._is_sec_valid(self.seconds + seconds):
			self.seconds += seconds
		else:
			raise ValueError

	def add_min(self, minutes):
		if my_time._is_min_valid(self.minutes + minutes):
			self.minutes += minutes
		else:
			raise ValueError
	
	def add_hour(self, hours):
		if my_time._is_hour_valid(self.hours + hours):
			self.hours += hours
		else:
			raise ValueError

	def _number_of_seconds(self):
		return self.seconds + self.minutes * 60 + self.hours * 3600	

    def __eq__(self, other):#=
        return self.microseconds == other.microseconds and \
        	self.seconds == other.seconds and \
        	self.minutes == other.minutes

    def __ne__(self, other):#!=
        return self.microseconds != other.microseconds or \
        	self.seconds != other.seconds or \
        	self.minutes != other.minutes 

    def __lt__(self, other):#<
        return self.microseconds < other.microseconds or \
        	(self.microseconds == other.microseconds and self.seconds < other.seconds) or \
        	(self.microseconds == other.microseconds and self.seconds == other.seconds and \
    		self.minutes < other.minutes) or \
    		(self.microseconds == other.microseconds and self.seconds == other.seconds and \
    		self.minutes == other.minutes and self.hours < other.hours) 
    	 
    def __le__(self, other):#<=
	    return self < other or self == other

    def __gt__(self, other):#>
        return self.microseconds > other.microseconds or \
        	(self.microseconds == other.microseconds and self.seconds > other.seconds) or \
        	(self.microseconds == other.microseconds and self.seconds == other.seconds and \
    		self.minutes > other.minutes) or \
    		(self.microseconds == other.microseconds and self.seconds == other.seconds and \
    		self.minutes == other.minutes and self.hours > other.hours)

    def __ge__(self, other):#>=
        return self > other or self == other		

	@staticmethod
	def _is_msec_valid(microseconds):
		if my_time._MIN_MSEC <= microseconds <= my_time._MAX_MSEC:
			return True
		else: 
			return False

	@staticmethod
	def _is_sec_valid(seconds):
		if my_time._MIN_SEC <= seconds <= my_time._MAX_SEC:
			return True
		else:
			return False

	@staticmethod
	def _is_min_valid(minutes):
		if my_time._MIN_MIN <= minutes <= my_time._MAX_MIN:
			return True
		else:
			return False				

	@staticmethod
	def _is_hour_valid(hours):
		if my_time._MIN_HOUR <= hours <= my_time._MAX_HOUR:
			return True
		else:
			return False		

	@staticmethod
	def _is_time_valid(microseconds, seconds, minutes, hours):
		if my_time._is_msec_valid(microseconds) and \
			my_time._is_sec_valid(seconds) and \
			my_time._is_min_valid(minutes) and \
			my_time._is_hour_valid(hours):
				return True
		else:
			return False
		

