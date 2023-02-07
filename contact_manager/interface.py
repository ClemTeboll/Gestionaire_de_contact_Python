from tkinter import *
from contact_model import ContactModel
from contact_manager import ContactManager

new_contact_manager = ContactManager()

window = Tk()

window.geometry('1200x600')
window.title('Gestionnaire de contacts')
window.configure(background = '#FFF')

title_label = Label(window, text='Gestionnaire de contact')
title_label.pack(pady=50)


def validate_values():
    contact_name = name_input_value.get()
    contact_surname = surname_input_value.get()
    contact_email = email_input_value.get()
    new_contact_model = ContactModel(contact_name, contact_surname, contact_email)
    print(new_contact_model.surname, new_contact_model.name, new_contact_model.email)


surname_input_value = StringVar()
name_input_value = StringVar()
email_input_value = StringVar()

surname_label = Label(window, text="Prénom").pack()
surname_input = Entry(window, textvariable=surname_input_value).pack()
error_surname_message = Label(window, text="")

name_label =  Label(window, text="Nom").pack()
name_input = Entry(window, textvariable=name_input_value).pack()
error_name_message = Label(window, text="")

email_label = Label(window, text="Email").pack()
email_input = Entry(window, textvariable=email_input_value).pack()
error_email_message = Label(window, text="")

validation_button = Button(window, text='Valider', command=validate_values).pack()


window.mainloop()