from contact_model import ContactModel

class ContactManager(ContactModel):
    def __init__(self, name, surname, email, newList):
        super().__init__(name, surname, email)
        self.contactList = newList if newList else []

    def show_contact_list(self):
        pass

    def add_contact(self):
        pass

    def set_item_in_list(self):
        pass

    def delete_contact(self):
        pass

    def modify_contact(self):
        pass