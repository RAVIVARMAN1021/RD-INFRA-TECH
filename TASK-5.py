class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {
            'Phone': phone,
            'Email': email,
            'Address': address
        }
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for name, info in self.contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {info['Phone']}")
                print(f"Email: {info['Email']}")
                print(f"Address: {info['Address']}")

    def search_contact(self, keyword):
        found = False
        for name, info in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in info['Phone']:
                print(f"\nMatch Found:")
                print(f"Name: {name}")
                print(f"Phone: {info['Phone']}")
                print(f"Email: {info['Email']}")
                print(f"Address: {info['Address']}")
                found = True
        if not found:
            print("No matching contact found.")

    def update_contact(self, name):
        if name in self.contacts:
            print("Enter new details (leave blank to keep current):")
            phone = input("New Phone: ") or self.contacts[name]['Phone']
            email = input("New Email: ") or self.contacts[name]['Email']
            address = input("New Address: ") or self.contacts[name]['Address']

            self.contacts[name] = {
                'Phone': phone,
                'Email': email,
                'Address': address
            }
            print(f"Contact '{name}' updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print("Contact not found.")

def menu():
    cb = ContactBook()
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            cb.add_contact(name, phone, email, address)

        elif choice == '2':
            cb.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone to search: ")
            cb.search_contact(keyword)

        elif choice == '4':
            name = input("Enter the name to update: ")
            cb.update_contact(name)

        elif choice == '5':
            name = input("Enter the name to delete: ")
            cb.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

menu()
