from controller import *
from model.da import *
from model.entity import *


class ProfileController:
    @classmethod
    def save(cls, name, family, email, password):
        try:
            da = ProfileDa()
            if not da.find_by_email(email):
                profile = Profile(name, family, email, password)
                da.save(profile)
                return True, profile
            else:
                raise DuplicateEmailError("Duplicate email")

        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name, family, email, password):
        try:
            da = ProfileDa()
            profile = Profile(name, family, email, password)
            profile.id = id
            da.edit(profile)
            return True, profile
        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = ProfileDa()
            profile = da.find_by_id(Profile, id)
            return True, da.remove(profile)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = ProfileDa()
            return True, da.find_all(Profile)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = ProfileDa()
            profile = da.find_by_id(Profile, id)
            if profile:
                return True,profile
            else:
                raise NoContentError("There is no profile!")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_email(cls, email):
        try:
            da = ProfileDa()
            return True, da.find_by_email(email)
        except Exception as e:
            return False, str(e)

    @classmethod
    def login(cls, email, password):
        try:
            da = ProfileDa()
            profile = da.find_by_email_password(email, password)
            if (profile):
                return True, profile
            else:
                raise AccessDeniedError("Wrong email/password")
        except Exception as e:
            return False, str(e)
