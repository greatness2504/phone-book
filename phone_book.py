# let the phone book be an empty dictionary that will be modified later on
phone_book = {}

# define a function for the contact
def add_contact():
    full_name = input("Enter your full name: ").title().strip()
    phone_number = input("Enter your phone number: ")
    sex = input("Enter sex: ").title()
    home_address = input("Enter you home address: ")
    
    contact = {
        "full_name" : full_name,
        "phone_number": phone_number,
        "sex" : sex,
        "home_address" : home_address
    }
    contact = phone_book
    print("Contact added successfully! ")
    
# a function to search for contacts
def search_contact():
    search_name = input("Enter a name to search for: ")
    if search_name in phone_book:
        contact = phone_book[search_name]
        print("Phone number:", contact['phone_number'])
        print("Sex:", contact['sex'])
        print("Home address:", contact['home_address'])
    else:
        print("Contact not found!")

# keep askin the user to add contacts to the phonebook
while True:
    print("Phone Book")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Quit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
        
    # break out of the loop when the user enters quit
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
