from model.entity import *
from model.da import *

da = DatabaseManager()

# ------------ SAVE , EDIT , REMOVE ------------------

#profile1 = Profile("mani", "dgm", "m@gmail.com", "m123")
#profile1.id = 1
#da.save(profile1)

#profile = da.find_by_id(Profile,1)
#profile.name = "<NAME>"
#profile.family = "<family>"
#profile.email = "<email>"
#profile.password = "<password>"
#da.edit(profile)
#da.remove(profile)

#task1 = Task("gym", profile1)
#task1.id = 1
#task1.status = True
#da.save(task1)

#task2 = Task("new task", profile1)
#task2.id = 2
#task2.status = False
#da.save(task2)


# ------------- FIND -----------------

#profile_list = da.find_all(Profile)
#for profile in profile_list:
    #print(profile.name, profile.family)

#profile = da.find_by_id(Profile,2)
#print(profile.id, profile.name, profile.family)


#task_list = da.find_all(Task)
#for task in task_list:
    #print(task.id, task.title, task.status, task.date_time, task.profile_id)




