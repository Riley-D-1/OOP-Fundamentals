from class_classes import * 

def menu():
    invalid_selection = True
    while invalid_selection:
        print("****************** Main Menu ********************")
        print()
        print("1. Create a New Class")
        print("2. Add a Student to a Class")
        print("3. Find a Student in a Class")
        print("4. Quit")
        print()
        try:
            menu_option = int(input("Select an option: "))
            if 1 <= menu_option <= 4:
                invalid_selection = False
            else:
                print("Please select a valid option from 1 to 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return menu_option
    
def main():
    classrooms = []
    while True:
        menu_option = menu()
        if menu_option == 4:
            break
            
        elif menu_option == 1:
            new_class_title = input("Enter the title of your class: ")
            classrooms.append(Classroom(new_class_title))
            print("Class created")
        
main()