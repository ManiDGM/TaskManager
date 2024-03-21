from model.entity import *
from model.da import *

da = DatabaseManager()

# ------------ SAVE ------------------

profile1 = Profile("mani", "dgm")
profile1.id = 1
da.save(profile1)


#profile2 = Profile("new", "new")
#profile2.id = 2
#da.save(profile2)

task1 = Task("gym", profile1)
task1.id = 1
da.save(task1)


# ------------- FIND -----------------

#profile_list = da.find_all(Profile)
#for profile in profile_list:
    #print(profile.name, profile.family)

#profile = da.find_by_id(Profile,2)
#print(profile.id, profile.name, profile.family)

