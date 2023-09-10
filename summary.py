import datetime


class Summary:
    def __init__(self, id, start_date, end_date=None, duration=None, late=None, damaged=None):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.duration = duration
        self.late = late
        self.damaged = damaged

    def __str__(self):
        return f"Summary({self.id}, {self.start_date}, {self.end_date}, {self.duration}, {self.late}, {self.damaged})"
