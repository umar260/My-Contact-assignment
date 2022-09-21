# Main Program Loop
def getMenuSelection():
    print("\nMAIN MENU")
    print("1:Display All Contact Names")
    print("2:Search for Contact")
    print("3:Edit Contact")
    print("4:New Contact")
    print("5:Remove contact")
    return str(input("Enter your selection:"))

users = [{
        "name": "Ben", 
        "phone": "555-5555", 
        "email": "Ben@mail.com"
    }, {
        "name": "Mr. V", 
        "phone": "444-4444", 
        "email": "mrv@mail.com"
    }, {
        "name": "Mr. Sam", 
        "phone": "444-4444", 
        "email": "Sam@mail.com"
    }];    

while True:
    x = getMenuSelection()
    if x == "1":
        for i in range(len(users)):
            print(users[i]["name"])
    elif x == "2":
        list = str(input("Enter the Name of the contact you want to search for:"))
        for i in users:
            if list == i["name"]:
                print(i)
                break
            print("Contact not found")
            break
    elif x == "3":
        list = str(input("Enter the Name of the contact you want to edit:"))
        for i in users:
            if list in i["name", "phone", "email"]:
                z = str(input("Enter the new name of the contact:"))
                i["name"] = z 
                i["phone"] = z
                i["email"] = z
                print("Contact edited")
                break
            print("Contact not found")
            break
    elif x == "4":
        list = input("Enter the Name of the contact you want to add:")
        for i in users:
            if list in i["name"]:
                print("Contact already exists")
                break
            else:
                z = input("Enter the phone number of the contact:")
                a = input("Enter the email of the contact:")
                users.append({"name": list, "phone": z, "email": a})
                print("Contact added")
                break
    elif x == "5":
        list = input("Enter the Name of the contact you want to remove:")
        for i in users:
            if list in i["name"]:
                users.remove(i)
                print("Contact removed")
                break
            print("Contact not found")
            break
    else:
        x = 0
        break


print(users)


