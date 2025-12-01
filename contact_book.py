# Task 5: Contact Book - CodSoft

import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    try:
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def show_menu():
    print("\n" + "=" * 40)
    print("            CONTACT BOOK")
    print("=" * 40)
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contact")
    print("4. Edit contact")
    print("5. Delete contact")
    print("6. Exit")


def list_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
        return

    print("\nContacts:")
    print("-" * 60)
    for idx, c in enumerate(contacts, start=1):
        print(f"ID: {idx}")
        print(f"  Name : {c.get('name')}")
        print(f"  Phone: {c.get('phone')}")
        print(f"  Email: {c.get('email')}")
        print(f"  Address: {c.get('address')}")
        print("-" * 60)


def add_contact(contacts):
    print("\nAdd New Contact")
    name = input("Name      : ").strip()
    phone = input("Phone     : ").strip()
    email = input("Email     : ").strip()
    address = input("Address   : ").strip()

    if not name or not phone:
        print("Name and phone are required.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email if email else "-",
        "address": address if address else "-",
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")


def get_index(contacts):
    if not contacts:
        print("No contacts available.")
        return None
    try:
        cid = int(input("Enter contact ID: "))
        if 1 <= cid <= len(contacts):
            return cid - 1
        print("Invalid ID.")
        return None
    except ValueError:
        print("Enter a valid number.")
        return None


def search_contact(contacts):
    keyword = input("\nEnter name or phone to search: ").lower().strip()
    results = [c for c in contacts if keyword in c["name"].lower() or keyword in c["phone"]]

    if not results:
        print("No matching contacts found.")
        return

    print("\nSearch Results:")
    print("-" * 60)
    for c in results:
        print(f"Name : {c['name']}")
        print(f"Phone: {c['phone']}")
        print(f"Email: {c['email']}")
        print(f"Address: {c['address']}")
        print("-" * 60)


def edit_contact(contacts):
    print("\nEdit Contact")
    list_contacts(contacts)
    idx = get_index(contacts)
    if idx is None:
        return

    c = contacts[idx]
    print("Leave blank to keep existing value.")
    new_name = input(f"New name ({c['name']}): ").strip()
    new_phone = input(f"New phone ({c['phone']}): ").strip()
    new_email = input(f"New email ({c['email']}): ").strip()
    new_address = input(f"New address ({c['address']}): ").strip()

    if new_name:
        c["name"] = new_name
    if new_phone:
        c["phone"] = new_phone
    if new_email:
        c["email"] = new_email
    if new_address:
        c["address"] = new_address

    save_contacts(contacts)
    print("Contact updated.")


def delete_contact(contacts):
    print("\nDelete Contact")
    list_contacts(contacts)
    idx = get_index(contacts)
    if idx is None:
        return

    deleted = contacts.pop(idx)
    save_contacts(contacts)
    print(f"Deleted contact: {deleted['name']}")


def main():
    contacts = load_contacts()

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            list_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            edit_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 6.")


if __name__ == "__main__":
    main()
