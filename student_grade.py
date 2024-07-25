student = { "Name": "Grade"}
def add_student(name, grade):
    student[name] = grade
    print(f"added {name} with {grade}")

def update_student(name, grade):
    if name in student:
        student[name] = grade
        print(f"{name} with marks updated {grade}")
    else:
        print(f"{name} is not found in record")

def delete_student(name):
    if name in student:
        del student[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found in record")

def display_student():
    for name, grade in student.items():
        print("----------------------")
        print(f"{name} :      {grade}")

def main():
    while True:
        print("\nStudent grade management System")
        print("1. Add student")
        print("2. Update grade")
        print("3. Delete student")
        print("4. View student")
        print("5. Exit")

        choice = int(input("Enter your choice "))
        if choice == 1:
            name = input("Enter the name of student: ")
            grade = input("Enter the grade of student: ")
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter the name of student: ")
            grade = input("Enter the grade of student: ")
            update_student(name, grade)
        elif choice == 3:
            name = input("Enter the name of student: ")
            delete_student(name)
        elif choice == 4:
            display_student()
        elif choice == 5:
            print("Record is closing")
            break
        else:
            print("Invalid Choice")

main()