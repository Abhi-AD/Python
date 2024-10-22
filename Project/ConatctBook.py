# Contact Book


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = {"name": name, "phone": phone, "email": email}
        self.contacts.append(contact)
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for index, contact in enumerate(self.contacts, 1):
            print(
                f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}"
            )

    def search_contact(self, search_term):
        found_contacts = [
            contact
            for contact in self.contacts
            if search_term.lower() in contact["name"].lower()
        ]
        if not found_contacts:
            print("No contacts found.")
        else:
            for index, contact in enumerate(found_contacts, 1):
                print(
                    f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}"
                )

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")
                return
        print(f"Contact {name} not found.")


def main():
    book = ContactBook()

    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            book.add_contact(name, phone, email)

        elif choice == "2":
            book.view_contacts()

        elif choice == "3":
            search_term = input("Enter name to search: ")
            book.search_contact(search_term)

        elif choice == "4":
            name = input("Enter name to delete: ")
            book.delete_contact(name)

        elif choice == "5":
            print("Exiting Contact Book.")
            break

        else:
            print("Invalid option. Please choose a valid one.")


if __name__ == "__main__":
    main()
