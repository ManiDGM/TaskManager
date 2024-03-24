from model.da import *
from model.entity import *

class TaskController:
    @classmethod
    def save(cls, title):
        try:
            da = TaskDa()
            task = Task(title)
            da.save(task)
            return task
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, profile_id,  title):
        try:
            da = TaskDa()
            task = Task(title)
            task.id = id
            task.profile_id = profile_id
            da.edit(task)
            return task
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = TaskDa()
            task = da.find_by_id(Task, id)
            if task:
                da.remove(task)
                return True
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_time(cls, datetime1, datetime2):
        try:
            da = TaskDa()
            task_list = da.find_by_time(datetime1, datetime2)
            return task_list
        except Exception as e:
            return False, str(e)


    @classmethod
    def find_by_profile_id(cls, profile_id):
        try:
            da = TaskDa()
            task_list = da.find_by_profile_id(profile_id)
            return task_list
        except Exception as e:
            return False, str(e)


