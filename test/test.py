from model.entity import *
from model.da import *

da = DatabaseManager()

profile1 = Profile("mani", "dgm")
profile1.id = 1
da.save(profile1)


profile2 = Profile("new", "new")
profile2.id = 2
da.save(profile2)
