import re
from exceptions_model import *

class ContactModel:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def check_name(self, name):
        try:
            if (name.len >= 2):
                return name
        except:
            raise InvalidContactNameException()

    def check_surname(self, surname):
        try:
            if (surname.len >= 2):
                return surname
        except:
            raise InvalidContactSurnameException()

    def check_email(self, email):
        regex = r'/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/'

        try:
            if (not re.fullmatch(regex, email)):
              return email
        except:
            raise InvalidContactEmailException()