from sqlalchemy import Column, Integer, String
from model.entity import *
from sqlalchemy.orm import relationship



class Profile(Base):
    __tablename__ = "profile_tbl"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    email = Column(String(500), unique=True)
    password = Column(String(500))


    def __init__(self, name, family, email, password):
        self.name = name
        self.family = family
        self.email = email
        self.password = password