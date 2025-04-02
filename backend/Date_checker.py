from datetime import datetime

class DateChecker:
    def __init__(self, current_date, new_date, date_format="%d %b, %y"):
        self.current_date = datetime.strptime(current_date, date_format)
        self.new_date = datetime.strptime(new_date, date_format)

    def is_new_date_earlier(self):
        """Returns True if new_date is before current_date, else False."""
        return self.new_date < self.current_date
