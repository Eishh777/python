# Contact phone book diary
contact = {}

# Operations
add = 1
delete = 2
search = 3
update = 4
display = 5
exit_program = 6

while True:
    print("\nOptions:")
    print("1 - Add Contact")
    print("2 - Delete Contact")
    print("3 - Search Contact")
    print("4 - Update Contact")
    print("5 - Display Contacts")
    print("6 - Exit")
    
    enter = int(input("Enter the operation (1-6): "))

    if enter == add:
        n = int(input("Enter the number of contacts you want to add: "))
        for _ in range(n):
            name = input("Enter name for the contact: ")
            num = input("Enter phone number: ")  # Use input to read as string
            contact[name] = num  # Store as string

    elif enter == delete:
        name = input("Enter the name of the contact you want to delete: ")
        if name in contact:
            del contact[name]
            print(f"Contact {name} deleted.")
        else:
            print("Contact not found.")

    elif enter == search:
        name = input("Enter the name of the contact you want to search: ")
        if name in contact:
            print(f"{name}: {contact[name]}")
        else:
            print("Contact not found.")

    elif enter == update:
        name = input("Enter the name of the contact you want to update: ")
        if name in contact:
            num = input("Enter the new phone number: ")
            contact[name] = num  # Update the contact
            print(f"Contact {name} updated.")
        else:
            print("Contact not found.")

    elif enter == display:
        if not contact:
            print("Your contact list is empty.")
        else:
            print("Contacts in your list:")
            for name, num in contact.items():  # Use .items() to iterate
                print(f"{name}: {num}")

    elif enter == exit_program:
        print("Exiting the program.")
        break

    else:
        print("Select an appropriate number!")