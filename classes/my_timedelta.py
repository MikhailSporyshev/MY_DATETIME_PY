class my_timedelta:
    _MIN_MSEC = 0
    _MAX_MSEC = 999999
    _MIN_SEC = 0
    _MAX_SEC = 3600 * 24 - 1
    _MIN_DAY = -999999999
    _MAX_DAY = 999999999
    
    def __init__(self, days=0, seconds=0):
        if my_timedelta._is_timedelta_valid(days,seconds):
            self.days = days
            self.seconds = seconds


    @staticmethod    
    def _is_day_valid(days):
        if day >= my_timedelta._MIN_DAY and day <= my_timedelta._MAX_DAY:
            return True
        return False    

    @staticmethod
    def _is_sec_valid(seconds):
        if my_timedelta._MIN_SEC <= sc <= my_timedelta._MAX_SEC:
            return True
        else:
            return False

    @staticmethod
    def _is_timedelta_valid(days, seconds):
        if my_timedelta._is_day_valid(days) and my_timedelta._is_sec_valid(seconds):
            return True
        else:
            return False


    