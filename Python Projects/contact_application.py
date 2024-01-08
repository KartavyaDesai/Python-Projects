#Contacts app
my_contacts = {}
def add(name, num):
    my_contacts.update({name:num})
def show():
    for key in my_contacts:
        print(key," --> ",my_contacts[key],"\n")
def delete(item):
    my_contacts.pop(item)
while True:
    todo = input("Welcome! What you want to do?\nTo add a new contact type \"new\"\nTo delete a contact type \"delete\"\nTo show stored contact type\"show\"\n\n").strip().lower()
    match todo:
        case "new":
            cont_name = input("Contact Name: ").title()
            cont_num = input("Number: ")
            add(cont_name, cont_num)
        case "show":
            show()
        case "delete":
            show()
            contact_name = input("Enter name of the contact to delete: ").title()
            delete(contact_name)
        case _:
            break
print("Thank you for using the application.")
