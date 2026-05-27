# Contact Book Application

contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact Added Successfully!\n")


def view_contacts():
    if len(contacts) == 0:
        print("No Contacts Found!\n")
    else:
        print("\nContact List")
        print("-" * 40)

        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        print()


def search_contact():
    search = input("Enter Name or Phone Number to Search: ")

    found = False

    for contact in contacts:
        if search.lower() == contact['name'].lower() or search == contact['phone']:
            print("\nContact Found")
            print("-" * 40)
            print("Name    :", contact['name'])
            print("Phone   :", contact['phone'])
            print("Email   :", contact['email'])
            print("Address :", contact['address'])
            print()

            found = True
            break

    if not found:
        print("Contact Not Found!\n")


def update_contact():
    name = input("Enter Name to Update: ")

    found = False

    for contact in contacts:
        if name.lower() == contact['name'].lower():

            print("Enter New Details")

            contact['phone'] = input("New Phone Number: ")
            contact['email'] = input("New Email: ")
            contact['address'] = input("New Address: ")

            print("Contact Updated Successfully!\n")

            found = True
            break

    if not found:
        print("Contact Not Found!\n")


def delete_contact():
    name = input("Enter Name to Delete: ")

    found = False

    for contact in contacts:
        if name.lower() == contact['name'].lower():
            contacts.remove(contact)

            print("Contact Deleted Successfully!\n")

            found = True
            break

    if not found:
        print("Contact Not Found!\n")


while True:

    print("===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid Choice! Please Try Again.\n")