# Main Program Loop
    def (main):
        list =[Umar, Ali, Sam]
        print(list)

    loop = True
    while loop:
        selection = getMenuSelection()

        if selection == "Umar":
            printUmars(Umar)
        elif selection == "Ali":

        elif selection == "3":
            
        elif selection == "4":
            
        elif selection == "5":
            loop = False
        else:
            print("Invalid selection")

    def getMenuSelection():
    print("\nMAIN MENU")
    print("1: Display All Grades")
    print("2: Display Honours")
    print("3: Stats")
    print("4: Randomize Grades")
    print("5: Exit")

    def printUmar(Umars):
        print("\nAll information about contact name Umar")
        for Umar in  Umars:
            print("Name = Umar")
            print("Phone#= 0301447038")
            print("email = umar780@Yahoo.com")

