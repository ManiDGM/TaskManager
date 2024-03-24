from model.da.database import DatabaseManager,and_,or_,between
from model.entity import *


class TaskDa(DatabaseManager):
    def find_by_title(self, title):
        self.make_engine()
        result = self.session.query(Task).filter(Task.title == title).all()
        if result:
            return result[0]
        else:
            return None

    def find_by_time(self, start_time, end_time):
        self.make_engine()
        result = self.session.query(Task).filter(between(Task.date_time >= start_time, Task.date_time <= end_time))
        self.session.close()
        return result
