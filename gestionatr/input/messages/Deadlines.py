from collections import namedtuple
from datetime import datetime, timedelta
from workdays import workday


class DeadLine(namedtuple('Deadline', "step, days")):
    def limit(self, date=None):
        if not date:
            date = datetime.today()
        # cut microseconds
        date = date.replace(microsecond=0)
        if isinstance(self.days, Naturaldays):
            return date + timedelta(self.days)
        else:
            return workday(date, self.days)


class Workdays(int):
    def __new__(cls, *args, **kwargs):
        return super(Workdays, cls).__new__(cls, *args, **kwargs)


class Naturaldays(int):
    def __new__(cls, *args, **kwargs):
        return super(Naturaldays, cls).__new__(cls, *args, **kwargs)


class ProcessDeadline(object):

    steps = []

    @classmethod
    def get_deadline(cls, step, modifier=None):
        if modifier:
            steps = getattr(cls, 'steps_{0}'.format(modifier))
        else:
            steps = cls.steps
        for s in steps:
            if s.step == step:
                return s
