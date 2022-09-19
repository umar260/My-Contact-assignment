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
print(users)

for i in range(len(users)):
    print(users[i]["name"])
x=getMenuSelection()
if x=="2":
    y=input("Enter the Name of the contact you want to search for:")
    if y in users:
        print(users[y])
    else:
        print("Contact not found")
