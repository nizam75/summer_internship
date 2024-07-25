students = { }
def add_student(name, grade):
    students[name] = grade
    print(f"{name} added with grade {grade}")

def update_student(name, grade):
    if name in students:
        students[name] = grade
        print(f"{name} updated with grade {grade}")
    else:
        print(f"{name} is not found in record")

def delete_student(name):
    if name in students:
        del students[name]
        print(f"{name} has been deleted successfully")
    else:
        print(f"{name} is not found in record")

def dispaly_student():
    for name, grade in students.items():
        print("--------------------")
        print(f"{name} :    {grade}")
def main():
    while True:
        print("1. : Add Record")
        print("2. : Update Record")
        print("3. : Delete Record")
        print("4. : Display Record")
        print("5. : Exit")
        choice = int(input("Enter the choice: "))
        if choice == 1:
            name = input("Enter the name of student: ")
            grade = input("Enter the grade of student:")
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter the name of student: ")
            grade = input("Enter the grade of student:")
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter the name of student you want to delete : ")
            delete_student(name)

        elif choice == 4:
            dispaly_student()

        elif choice == 5:
            print("Record is closing")
            break
        else:
            print("Invalid choice")

main()




