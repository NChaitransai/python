contacts={}
def add_contact(name:str,mobile:int):
    if name not in contacts:
        contacts[name]=mobile
        return 'contact saved'
    return 'contact not saved'

def update_contact(name:str,mobile:int):

    if name in contacts:
        contacts[name]=mobile
        return 'contact updated'
    return 'contact doesnot exist '


def delete_contact(name:str):
    if name in contacts:
        contacts.pop(name)
        return 'contact deleted'
    return 'contact doesnot exist'

def get_mobile(name:str):
    if name in contacts:
        contacts.get(name,"contact not found")
        return 'contact found'
    return 'contact not found'

def All_contacts():
    return contacts


print(add_contact("chaitran",8639462003))
print(add_contact("harshit",9988895328))
print(add_contact('sachin',9087766553))
print(contacts)
print(update_contact("chaitran",8688740877))
print(contacts)
print(delete_contact("harshit" ""))
print(contacts)
print(All_contacts())