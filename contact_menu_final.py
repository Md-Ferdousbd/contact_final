import csv

# Define the filename to store the contacts
CONTACTS_FILE = 'contacts.csv'

# Function to load existing contacts from the CSV file
def load_contacts():
    contacts = []
    try:
        with open(CONTACTS_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            # Skip header
            next(reader)
            for row in reader:
                contacts.append({
                    'name': row[0],
                    'mobile': row[1],
                    'email': row[2],
                    'location': row[3],
                    'company': row[4]
                })
    except FileNotFoundError:
        pass  # If file doesn't exist, return empty list
    return contacts

# Function to save contacts to the CSV file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['Name', 'Mobile', 'Email', 'Location', 'Company'])
        for contact in contacts:
            writer.writerow([contact['name'], contact['mobile'], contact['email'], contact['location'], contact['company']])

# Function to add a new contact
def add_contact():
    name = input("Enter the contact's name: ")
    mobile = input("Enter the mobile number: ")
    
    # Check if the mobile number already exists
    contacts = load_contacts()
    for contact in contacts:
        if contact['mobile'] == mobile:
            print("Error: This mobile number is already associated with another contact.")
            return  # Exit the function if duplicate is found
    
    email = input("Enter the email address: ")
    location = input("Enter the location: ")
    company = input("Enter the company: ")

    contact = {
        'name': name,
        'mobile': mobile,
        'email': email,
        'location': location,
        'company': company
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts available.")
        return
    print("\nAll Contacts:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Mobile: {contact['mobile']}, Email: {contact['email']}, Location: {contact['location']}, Company: {contact['company']}")

# Function to search for a contact by mobile number
def search_contact():
    search = input("Please enter the mobile number to search: ")
    contacts = load_contacts()

    found = False
    for contact in contacts:
        if contact['mobile'] == search:
            print("\nContact found:")
            print(f"Name: {contact['name']}")
            print(f"Mobile: {contact['mobile']}")
            print(f"Email: {contact['email']}")
            print(f"Location: {contact['location']}")
            print(f"Company: {contact['company']}")
            found = True
            break
    
    if not found:
        print("No contact found with the provided mobile number.")

# Function to remove a contact by mobile number
def remove_contact():
    remove_number = input("Please enter the mobile number of the contact to remove: ")
    contacts = load_contacts()

    new_contacts = [contact for contact in contacts if contact['mobile'] != remove_number]

    if len(new_contacts) == len(contacts):
        print("No contact found with the provided mobile number.")
    else:
        save_contacts(new_contacts)
        print("Contact removed successfully!")

# Main program loop
def main():
    while True:
        print("\n1. Add contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Remove contact")
        print("0. Exit contact")
        
        choice = input("Please input any number: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            remove_contact()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == '__main__':
    main()
