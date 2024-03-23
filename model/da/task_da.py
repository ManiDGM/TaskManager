from model.da.database import DatabaseManager,and_,or_,between
from model.entity import *


class TaskDa(DatabaseManager):
    def find_by_title(self, title):
        self.make_engine()
        result = self.session.query(Task).filter(Task.title == title).all()
        if result:
            return result[0]
