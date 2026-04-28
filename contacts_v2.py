#reading file content
import csv
def read_content():
    with open('content.csv','r')as file:
        reader_obj=csv.reader(file)
        return list(reader_obj)
contacts={}#for storing conacts
#add new contacts
def add_contact(name:str,moblie:int):
    #check whether name is exists in exists in contacts
    contacts=read_content()
    if name not in contacts:
        #add new contact to contacts
        contacts[name]=moblie
        return 'contact saved'
    return "contact name is already exists,check with another name...."

#update contact
def update_contact(name:str,mobile:int):
     #check whether name is exists in exists in contacts
    if name in contacts:
        #update mobile numbers in contacts
        contacts[name]=mobile
        return 'contact saved'
    return "contact name is not exists,check  name again....."


#delete contact
def delete_contact(name:str):
    #check whether name is exists in exists in contacts
    if name in contacts:
        #delete mobile numbers in contacts
        contacts.pop(name)
        return 'contact deleted...'
    return "contact name  not exists,check  name again....."

#get moblie number by searching name
def get_mobile(name:str):
   #check whether name is exists in exists in contacts


   return contacts.get(name, "contact name not eists check again")

#all contacts
def all_contacts():
    pass


if __name__=='__main__':
    print('Welcome to the contacts managerment')
    while True:
        print('select your operation \n 1.Add conatact \n 2.Update contact \n 3.Delete contact \n 4.Search mobile number by name \n 5.See all contacts \n 6.Exit')
        choice=int(input("Enter your choice :"))
        if choice==1:
            print('Your selected operation is 1. Add contact')
            name=input("Enter contact name:")
            mobile=int(input("Enter mobile number :"))
            res=add_contact(name,mobile)
            print(res)
        elif choice==2:
            print('Your selected operation is 2.Update contact')
            name=input("Enter contact name:")
            mobile=int(input("Enter mobile number :"))
            res=update_contact(name,mobile)
            print(res)
        elif choice==3:
            print('Your selected operation is 3. Delete contact')
            name=input("Enter contact name:")
            res=delete_contact(name)
            print(res)
        elif choice==4:
            print('Your selected operation is 4. Search mobile number by name')
            name=input("Enter contact name:")
            res=get_mobile(name)
            print(res)
        elif choice==5:
            print('Your selected operation is 5. See all contacts')
            res=all_contacts()
            for name, mobile in res.items():
                print(f"{name}:{mobile}")
        elif choice== 6:
            print("Your Exited from application Bye Bye..")
            exit()
        else:
            print("Invalid choice and selete choice between(1-6)")
     

