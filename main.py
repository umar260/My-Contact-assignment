
# Main Program Loop
def getMenuSelection():
    print("\nMAIN MENU")
    print("1:Display All Contact Names")
    print("2:Search for Contact")
    print("3:Edit Contact")
    print("4:New Contact")
    print("5:Remove contact")
    print("6:Exit")
    return str(input("Enter your selection:"))

users = [{
        "name": "Ben", 
        "phone": "555-5555", 
        "email": "Ben@mail.com"
    }, {
        "name": "V", 
        "phone": "444-4444", 
        "email": "v@mail.com"
    }, {
        "name": "Sam", 
        "phone": "444-4444", 
        "email": "Sam@mail.com"
    }];    

while True:
    selection = getMenuSelection()
    if selection == "1":
        for contact in users:
            print(contact["name"])

    elif selection=="2":
        print("Search for contact")
        name_search=input("Who's contact name do you want to search?: ")
        for i in users:
            if i["name"] == name_search:
                print("")
                print(i["name"])
                print(i["phone"])
                print(i["email"])
                break
        else:
            print("This name doesn't exist in contact list.")

    elif selection == "3":
        print("Edit contact")
        editname = input("Who's contact info do you want to change?: ")
        for i in users:
            if i["name"] == editname:
                editednumber = input("What is the new number?: ")
                i["phone"] = editednumber
                edited_email = input("What is the new email?: ")
                i["email"] = edited_email
                break
        else:
            print("This name doesn't exist in contact list.")

    elif selection=="4":
        print("New contact")
        newname = str(input("What is the name of your new contact?: "))
        newnumber = str(input("What is the number of your new contact?: "))
        newemail = str(input("What is the email of your new contact?: "))
        users.append({"name": newname, "phone": newnumber, "email": newemail})

    elif selection=="5":
        print("Remove Contact")
        removename=input("Which person name do you want to remove from contact list?: ")
        for i in users:
            if i["name"] == removename:
                users.remove(i)
                break
        else:
            print("This name doesn't exist in contact list.")

    elif selection == "6":
         print("EXITED")
         loop = False
