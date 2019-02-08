from contact import Contact


class PhoneBook:

    def __init__(self, name):
        self.name = name
        self.contact_list = list()

    def add_contact(self, name, surname, telephone, *args, **kwargs):
        self.contact_list.append(Contact(name, surname, telephone, *args, **kwargs))

    def delete_contact(self, number):
        for contact in self.contact_list:
            if number in contact.telephone or number in contact.additional:
                self.contact_list.remove(contact)

    def print_list(self):
        for contact in self.contact_list:
            print(contact)

    def print_favourites(self):
        for contact in self.contact_list:
            if contact.favourite is True:
                print(contact)

    def search_by_name(self, name):
        for contact in self.contact_list:
            if name in contact.name or name in contact.surname:
                print(contact)
