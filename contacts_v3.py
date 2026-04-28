import csv

def read_content():
    contacts = {}
    try:
        with open('content.csv', 'r') as file:
            reader_obj = csv.reader(file)
            for row in reader_obj:
                if len(row) == 2:
                    name, mobile = row
                    contacts[name] = int(mobile)
    except FileNotFoundError: pass  # If file doesn't exist, return empty dict
    return contacts

def write_content(contacts):
    with open('content.csv', 'w', newline='') as file:
        writer_obj = csv.writer(file)
        for name, mobile in contacts.items():
            writer_obj.writerow([name, mobile])

# Add new contacts
def add_contact(name: str, mobile: int):
    contacts = read_content()
    if name not in contacts:
        contacts[name] = mobile
        write_content(contacts)
        return 'contact saved'
    return "contact name is already exists, check with another name...."

# Update contact
def update_contact(name: str, mobile: int):
    contacts = read_content()
    if name in contacts:
        contacts[name] = mobile
        write_content(contacts)
        return 'contact updated'
    return "contact name is not exists, check name again....."

# Delete contact
def delete_contact(name: str):
    contacts = read_content()
    if name in contacts:
        del contacts[name]
        write_content(contacts)
        return 'contact deleted...'
    return "contact name not exists, check name again....."

# Get mobile number by searching name
def get_mobile(name: str):
    contacts = read_content()
    return contacts.get(name, "contact name not exists check again")

# All contacts
def all_contacts():
    return read_content()

if __name__ == '__main__':
    print('Welcome to the contacts management')
    while True:
        print('select your operation \n 1.Add contact \n 2.Update contact \n 3.Delete contact \n 4.Search mobile number by name \n 5.See all contacts \n 6.Exit')
        try:
            choice = int(input("Enter your choice :"))
        except ValueError:
            print("Invalid input. Please enter a number between 1-6.")
            continue
        if choice == 1:
            print('Your selected operation is 1. Add contact')
            name = input("Enter contact name:")
            try:
                mobile = int(input("Enter mobile number :"))
            except ValueError:
                print("Invalid mobile number. Please enter digits only.")
                continue
            res = add_contact(name, mobile)
            print(res)
        elif choice == 2:
            print('Your selected operation is 2. Update contact')
            name = input("Enter contact name:")
            try:
                mobile = int(input("Enter mobile number :"))
            except ValueError:
                print("Invalid mobile number. Please enter digits only.")
                continue
            res = update_contact(name, mobile)
            print(res)
        elif choice == 3:
            print('Your selected operation is 3. Delete contact')
            name = input("Enter contact name:")
            res = delete_contact(name)
            print(res)
        elif choice == 4:
            print('Your selected operation is 4. Search mobile number by name')
            name = input("Enter contact name:")
            res = get_mobile(name)
            print(res)
        elif choice == 5:
            print('Your selected operation is 5. See all contacts')
            res = all_contacts()
            if res:
                for name, mobile in res.items():
                    print(f"{name}:{mobile}")
            else:
                print("No contacts found.")
        elif choice == 6:
            print("You exited from application. Bye Bye..")
            break
        else:
            print("Invalid choice. Select choice between (1-6)")