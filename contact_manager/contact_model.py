import re

class ContactModel:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def check_name(self, name):
        if (name.len <= 2):
            print_name_response = print("Votre nom doit avoir plus de 2 caractères. Veuillez réessayer.")
            return print_name_response

        return name

    def check_surname(self, surname):
        if (surname.len <= 2):
            print_surname_response = print("Votre prénom doit avoir plus de 2 caractères. Veuillez réessayer.")
            return print_surname_response

        return surname

    def check_email(self, email):
        regex = r'/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/'

        if (re.fullmatch(regex, email)):
             print_name_response = print("Votre email n'est pas valide. Veuillez réessayer.")
             return print_name_response

        return email