import datetime


class Session:
    def __init__(self, id, start_time, end_time=None, duration=None, late=None, damaged=None):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.late = late
        self.damaged = damaged

    def __str__(self):
        return f"Summary({self.id}, {self.start_time}, {self.end_time}, {self.duration}, {self.late}, {self.damaged})"
