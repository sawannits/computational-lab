students = []
def insert_student():
    student_id = input("Enter Student ID: ")
    for student in students:
        if student["ID"] == student_id:
            print("Student ID already exists!")
            return
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    course = input("Enter Student Course: ")
    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course
    }
    students.append(student)
    print("Student record added successfully.")
def delete_student():
    student_id = input("Enter Student ID to delete: ")
    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print("Student record deleted successfully.")
            return
    print("Student not found.")
def search_student():
    student_id = input("Enter Student ID to search: ")
    for student in students:
        if student["ID"] == student_id:
            print("\n Student Found")
            for key, value in student.items():
                print(f"{key}: {value}")
            return
    print("Student not found.")
while True:
    print("\n Student Record Management System")
    print("1. Insert Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        insert_student()
    elif choice == "2":
        delete_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice! Please try again.")
