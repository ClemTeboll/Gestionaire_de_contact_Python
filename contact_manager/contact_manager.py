from contact_model import ContactModel

class ContactManager(ContactModel):
    def __init__(self, name, surname, email, currentList):
        super().__init__(name, surname, email)
        self.contactList = currentList if currentList else []

    def show_contact_list(self, displayList):
        pass

    def add_contact(self, contactToCreate):
        equivalence = lambda contact: contact, self.contactList
        checkContact = next(filter(equivalence, self.contactList), None)

        if (not checkContact):
            self.contactList.append(contactToCreate)
        else:
            print("Contact déjà existant")


    def set_item_in_list(self):
        pass

    def delete_contact(self):
        pass

    def modify_contact(self):
        pass