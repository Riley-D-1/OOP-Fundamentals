from subject import *
choice = 0
while choice != 4:
    choice = int(input("Pick an option:\n 1: Add a subject to a list \n 2: View a chosen subject from the list\n 3: View all subject details from the list \n 4: Exit \n"))
    if choice == 1:
        print("Meep")
    elif choice == 2:
        print("Filler")
    elif choice == 3:
        print("dave")
    else:
        pass
coding = Subject("Coding",3,"cod1",12)
print(coding.info())