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
        "name": "V", 
        "phone": "444-4444", 
        "email": "v@mail.com"
    }, {
        "name": "Sam", 
        "phone": "444-4444", 
        "email": "Sam@mail.com"
    }];    

while True:
    x = getMenuSelection()
    if x == "1":
        for i in range(len(users)):
            print(users[i]["name"])
    elif x == "2":
        search_name = input("Enter the Name of the contact you want to search for:")
        for user_dict in users:
            if search_name == user_dict["users"]:
                print(search_name)
                break
            print("Contact not found")
            break
    elif x == "3":
        search_name = str(input("Enter the Name of the contact you want to edit:"))
        for user_dict in users:
            if search_name == user_dict["name"]:
                user_dict["name"] = input("Enter the new name of the contact:")
                user_dict["phone"] = input("Enter new phone number:")
                user_dict["email"] = input("Enter new email:")
                print("Contact edited")
                break
            print("Contact not found")
            break
    elif x == "4":
        search_name = input("Enter the Name of the contact you want to add:")
        for user_dict in users:
            if search_name in user_dict["name"]:
                print("Contact already exists")
                break
            else:
                phone = input("Enter the phone number of the contact:")
                email = input("Enter the email of the contact:")
                users.append({"name": list, "phone": phone, "email": email})
                print("Contact added")
                break
    elif x == "5":
        Name_remove = input("Enter the Name of the contact you want to remove:")
        for user_dict in users:
            if Name_remove in user_dict["name"]:
                users.remove(user_dict)
                print("Contact removed")
                break
            print("Contact not found")
            break
    else:
        x = 0
        break


print(users)


