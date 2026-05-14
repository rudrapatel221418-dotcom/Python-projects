student={}

while True:

    print("......Student Manager App .....")
    print("1 ---> ADD STUDENT ")
    print("2 ---> VIEW STUDENT ")
    print("3 ---> CHECK RESULT ")
    print("4 ---> EXIT")

    choice= input("Enter your choice:-")

    if choice == "1":
        name= input("Enter Student Name:")
        marks=float(input("Enter marks:-"))
        student[name]= marks
        print(f"{name} is added sucessfully✅")

    elif choice == "2":
        if not student:
            print("NO STUDENT FOUND !!!")
        else:
            for name,marks in student.items():
                print(name,":",marks)


    elif choice == "3":
        name= input("Enter your name :- ")

        if name in student:
            marks = student[name]
            
            if marks >= 33 :
                print(f"{name} is passed in examination")
            else:
                print(f"{name} failed in examination......")
        else:

            print("Student not found!!!!!!!")
    elif choice == "4":
        print("Exited programme successfully")
        break

    