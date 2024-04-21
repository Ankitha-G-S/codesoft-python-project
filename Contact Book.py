class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword.lower() in contact.phone.lower()]
        for idx, contact in enumerate(results):
            print(f"{idx+1}. Name: {contact.name}, Phone: {contact.phone}")

    def update_contact(self, contact_index, new_contact):
        if 0 <= contact_index < len(self.contacts):
            self.contacts[contact_index] = new_contact
        else:
            print("Invalid contact index.")

    def delete_contact(self, contact_index):
        if 0 <= contact_index < len(self.contacts):
            del self.contacts[contact_index]
        else:
            print("Invalid contact index.")

def display_menu(contact_book):
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    return choice, contact_book

def main():
    contact_book = ContactBook()

    while True:
        choice, contact_book = display_menu(contact_book)

        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")

            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)

        elif choice == 2:
            contact_book.view_contact_list()

        elif choice == 3:
            keyword = input("Enter search keyword: ")
            contact_book.search_contact(keyword)

        elif choice == 4:
            contact_index = int(input("Enter contact index to update: ")) - 1
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")

            new_contact = Contact(name, phone, email, address)
            contact_book.update_contact(contact_index, new_contact)

        elif choice == 5:
            contact_index = int(input("Enter contact index to delete: ")) - 1
            contact_book.delete_contact(contact_index)

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
