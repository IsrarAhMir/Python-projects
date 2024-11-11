contacts = {}

while True:
    print("\n   Contact Book App")
    print("*==*==*==*==*==*==*==*")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contact")
    print("7.  Exit")

    choice =  input("Enter your choice: ")

    if choice == '1':
       name =  input("Enter name: ")

       if name  in contacts:
           print("Contact already exists")
       else:
           age = input("Enter age: ")
           email = input("Enter email: ")
           phoneNo = input("Enter phone number: ")
           storeName = input("Enter Store Name: ")
           address =  input("Enter address: ")
           contacts[name] = {"age": int(age),
                            "email": email,
                            "phoneNo": phoneNo,
                            "storeName": storeName,
                            "address": address}
           print(f"Contact name {name} has  been added successfully")

    elif choice  == '2':
        name =  input("Enter name to view: ")
        if name in contacts:

            contact_details = contacts[name]
            age = contact_details.get('age', 'N/A')
            email = contact_details.get('email', 'N/A')
            phoneNo = contact_details.get('phoneNo', 'N/A')
            storeName = contact_details.get('storeName', 'N/A')
            address = contact_details.get('address', 'N/A')

            print(f"Name: {name}, Age: {age}, Email: {email}, Phone Number: {phoneNo}, Store Name: {storeName}, Address: {address}")
        else:
                print("Contact not found")

    
    elif choice == '3':
        name =  input("Enter name to update: ")
        if name in contacts:
            age = input("Enter updated age: ")
            email = input("Enter updated gmail: ")
            phoneNo = input("Enter updated  phone number: ")
            storeName = input("Enter updated store name: ")
            address =  input("Enter updated address: ")
            contacts[name] = {"age": int(age),
                            "email": email,
                            "phoneNo": phoneNo,
                            "storeName": storeName,
                            "address": address} 
        else:
            print("Contact not found")


    elif choice == "4":
        name =  input("Enter name to delete: ")
        if  name in contacts:
            del contacts[name]
            print(f"Contact name {name} has been deleted successfully")
        else:
            print("Contact not found")

    
    elif choice ==  "5":
        search_name = input("Enter  name to search: ")
        found = False 
        for name, contacts in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found - Name{name},Age:{age},Phone number{phoneNo}, Email{email},Store Name: {storeName}, Address: {address} ')
                found = True 

            if not found:
                print("No contact found")

    elif choice ==  "6":
        print(contacts)
        print(f"Total contacts in  the list: {len(contacts)}")
    
    elif choice ==  "7":
        print('Good bye....closing......the programme')
        break
    else :
        print("Invaled input")
        















           
           


