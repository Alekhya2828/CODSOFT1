# Contact management program
contacts = {}  # A dictionary to store contacts. The name will be the key, and the details (phone, email, address) will be the value.

# Function to add a new contact
def add_contact():
    # Ask the user to enter the contact details
    name = input("Enter contact name: ")  # The contact's name is entered
    phone = input("Enter phone number: ")  # The contact's phone number is entered
    email = input("Enter email address: ")  # The contact's email address is entered
    address = input("Enter address: ")  # The contact's address is entered
    
    # Store the contact in the dictionary with the name as the key and the details as the value
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added successfully!")  # Confirm the contact was added

# Function to view all contacts
def view_contacts():
    if contacts:  # If there are any contacts in the dictionary
        print("\nContact List:")
        for name, details in contacts.items():  # Loop through all contacts in the dictionary
            # Print the contact name and phone number
            print(f"Name: {name}, Phone: {details['phone']}")
    else:
        print("No contacts found.")  # If no contacts exist, inform the user

# Function to search for a contact by name or phone number
def search_contact():
    search_query = input("Enter name or phone number to search: ")  # Ask for the name or phone number to search
    found = False  # A flag to check if a match was found
    for name, details in contacts.items():  # Loop through all contacts
        # Check if the search query matches either the name or the phone number (case-insensitive for name)
        if search_query.lower() == name.lower() or search_query == details['phone']:
            # If a match is found, print the full contact details
            print(f"\nContact Found:\nName: {name}")
            print(f"Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True  # Set the flag to True to indicate a match was found
            break  # Exit the loop once a match is found
    if not found:  # If no match was found after looping through all contacts
        print("No contact found with that name or phone number.")  # Inform the user that no match was found

# Function to update an existing contact's details
def update_contact():
    name = input("Enter the name of the contact you want to update: ")  # Ask for the name of the contact to update
    if name in contacts:  # Check if the contact exists
        print("What would you like to update?")
        print("1. Phone")
        print("2. Email")
        print("3. Address")
        choice = input("Enter choice (1/2/3): ")  # Ask the user which detail they want to update
        
        if choice == '1':  # If the user chooses to update the phone number
            new_phone = input("Enter new phone number: ")  # Ask for the new phone number
            contacts[name]['phone'] = new_phone  # Update the phone number in the contact's details
        elif choice == '2':  # If the user chooses to update the email
            new_email = input("Enter new email address: ")  # Ask for the new email
            contacts[name]['email'] = new_email  # Update the email address
        elif choice == '3':  # If the user chooses to update the address
            new_address = input("Enter new address: ")  # Ask for the new address
            contacts[name]['address'] = new_address  # Update the address
        else:
            print("Invalid choice.")  # If the user chooses an invalid option, print an error message
        print(f"Contact '{name}' updated successfully!")  # Confirm the update
    else:
        print("Contact not found.")  # If the contact doesn't exist, inform the user

# Function to delete an existing contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")  # Ask for the name of the contact to delete
    if name in contacts:  # Check if the contact exists
        del contacts[name]  # Delete the contact from the dictionary
        print(f"Contact '{name}' deleted successfully!")  # Confirm the contact was deleted
    else:
        print("Contact not found.")  # If the contact doesn't exist, inform the user

# Main function that runs the Contact Management System
def main():
    while True:  # Run the program continuously until the user chooses to exit
        # Print the menu of available options
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        # Ask the user to choose an option
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        
        if choice == '1':  # If the user chooses to add a contact
            add_contact()  # Call the function to add a contact
        elif choice == '2':  # If the user chooses to view the contact list
            view_contacts()  # Call the function to view all contacts
        elif choice == '3':  # If the user chooses to search for a contact
            search_contact()  # Call the function to search for a contact
        elif choice == '4':  # If the user chooses to update a contact
            update_contact()  # Call the function to update a contact
        elif choice == '5':  # If the user chooses to delete a contact
            delete_contact()  # Call the function to delete a contact
        elif choice == '6':  # If the user chooses to exit
            print("Thank you for using the Contact Management System!")  # Print a goodbye message
            break  # Exit the program
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")  # If the user enters an invalid option, print an error

# Run the contact management system
main()
