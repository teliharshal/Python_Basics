students = []

while True:
    print("\n ==Student Management System==")
    print("Add Student")
    print("View Student's info")
    print("Search Student")
    print("Update Students info")
    print("Delete Student info")
    print("Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id =  int(input("Enter the Student's id: "))
        student_name = input("Enter the name of the student: ")
        email = input("Enter the email of the student: ")
        course = input("Enter the course name of the student: ")

        student = {
            "id": student_id,
            "name": student_name,
            "email": email,
            "course": course
        }

        students.append(student)
        print("data of a student added successfully")
        
    elif choice == "2":
        if len(students) == 0:
            print("no student found!")

        else:

            print("\n == student's list is == ")
            for n in students:
                print("id:",n["id"])
                print("name",n["name"])
                print("email",n["email"])
                print("course",n["course"])
                print("---------")

    elif choice == "3":
        searched_id = int(input("Enter the id of the student: "))
        found = False

        for n in students:
            if n["id"] == searched_id:
                print("ID:",n["id"])
                print("name",n["name"])
                print("email",n["email"])
                print("couse",n["course"])
                print("-----------")

                found = True
                break

        if found == False:
            print("Student Not found")


    elif choice == "4":
         update_id = int(input("Enter a student id to be update: "))
         found = False
         for n in students:
             if n["id"] == update_id:
                 print("Student Found")
                 n["name"] = input("Edit the name of the student: ")
                 n["email"] = input("Enter or change the email of the student")
                 n["course"] = input("Enter or change the course name of the student")

                 found = True
                 break
         
         if found == False:
             print("Student not found! ")
             
    elif choice == "5":
        delete_id = int(input("Enter the id to delete a student: "))
        found = False

        for n in students:
            if n["id"] == delete_id:
                n["id"] = students.remove(n)

            found = True
            print("Student deleted successfully!")
            break

        if found == False:
            print("Student not found!")
         
    elif choice == "6":
        print("exit")
        break

    else:
        print("Invalid choice! Please select between 1 and 6.")





