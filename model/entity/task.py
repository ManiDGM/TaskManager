from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model.entity import *

class Task(Base):
    __tablename__ = "task"


    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    date_time = Column(DateTime)
    status = Column(Boolean)
    profile_id = Column(Integer, ForeignKey("profile.id"))

    profile = relationship("Profile")

    def __init__(self, title, profile):
        self.title = title
        self.date_time = datetime.now()
        self.profile = profile
