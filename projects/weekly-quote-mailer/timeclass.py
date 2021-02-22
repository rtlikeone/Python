import datetime as dt


class Time():
    def __init__(self):
        super().__init__()
        self.now = dt.datetime.now()
        self.year = self.now.year
        self.month = self.now.month
        self.day = self.now.weekday()
