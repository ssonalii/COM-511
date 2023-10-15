# Initialize the student database as an empty list of dictionaries
student_database = []

# Function to add a student record to the database
def add_student_record():
    student = {}
    student["roll_number"] = input("Enter Roll Number: ")
    student["name"] = input("Enter Name: ")
    student["age"] = input("Enter Age: ")
    student_database.append(student)
    print(f"Student '{student['name']}' added to the database.")

# Function to search for a student record by roll number
def search_student_record(roll_number):
    for student in student_database:
        if student["roll_number"] == roll_number:
            return student
    return None  # Student not found

# Function to update a student record
def update_student_record(roll_number):
    student = search_student_record(roll_number)
    if student:
        print("Updating student record:")
        student["name"] = input("Enter updated Name: ")
        student["age"] = input("Enter updated Age: ")
        print(f"Student record for Roll Number {roll_number} updated.")
    else:
        print("Student not found!")

# Function to delete a student record
def delete_student_record(roll_number):
    student = search_student_record(roll_number)
    if student:
        student_database.remove(student)
        print(f"Student record for Roll Number {roll_number} deleted.")
    else:
        print("Student not found!")

# Function to display all student records
def display_student_records():
    if not student_database:
        print("The database is empty.")
    else:
        print("Student Records in the database:")
        for i, student in enumerate(student_database, start=1):
            print(f"{i}. Roll Number: {student['roll_number']}, Name: {student['name']}, Age: {student['age']}")

# Main program
while True:
    print("\nStudent Database Management")
    print("1. Add Student Record")
    print("2. Search Student Record")
    print("3. Update Student Record")
    print("4. Delete Student Record")
    print("5. Display Student Records")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student_record()

    elif choice == "2":
        roll_number = input("Enter Roll Number to search: ")
        student = search_student_record(roll_number)
        if student:
            print("Student Record found:")
            print(f"Roll Number: {student['roll_number']}, Name: {student['name']}, Age: {student['age']}")
        else:
            print("Student not found!")

    elif choice == "3":
        roll_number = input("Enter Roll Number to update: ")
        update_student_record(roll_number)

    elif choice == "4":
        roll_number = input("Enter Roll Number to delete: ")
        delete_student_record(roll_number)

    elif choice == "5":
        display_student_records()

    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option (1, 2, 3, 4, 5, or 6).")