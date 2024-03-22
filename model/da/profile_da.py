from model.da.database import DatabaseManager,and_,or_,between
from model.entity import *


class ProfileDa(DatabaseManager):
    def find_by_email_password(self, email, password):
        self.make_engine()
        result = self.session.query(Profile).filter(
            and_(Profile.email == email, Profile.password == password)).all()
        if result:
            return result[0]

    def find_by_email(self, email):
        self.make_engine()
        result = self.session.query(Profile).filter(Profile.email == email).all()
        if result:
            return result[0]
