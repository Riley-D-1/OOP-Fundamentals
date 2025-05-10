from subject import *
choice = 0
subject_list = []
while choice != 4:
    choice = int(input("Pick an option:\n 1: Add a subject to a list \n 2: View a chosen subject from the list\n 3: View all subject details from the list \n 4: Exit \n"))
    if choice == 1:
        name = input("What is the name of subject? ")
        year = input("What is the year lvl of subject? ")
        code = input("What is the code of subject? ")
        student_num = input("What is the number of students in subject? ")
        
        new = Subject(name, year, code, student_num)
        subject_list.append(new)
    elif choice == 2:
        vaule = input("Type the number of the subject you want to view the infomation of: ")
        print(subject_list[int(vaule)-1].info())
    elif choice == 3:
        for item in subject_list:
            print(item.info())
    else:
        pass
