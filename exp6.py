# Initialize an empty list to store student records (each student is represented by a dictionary)
student_records = []

# Function to add a student record to the list
def add_student_record():
    student = {}
    student["roll_number"] = input("Enter Roll Number: ")
    student["name"] = input("Enter Name: ")
    student["age"] = input("Enter Age: ")
    student_records.append(student)

# Function to search for a student record by roll number
def search_student_record(roll_number):
    for student in student_records:
        if student["roll_number"] == roll_number:
            return student
    return None  # Student not found

# Function to display a student's record
def display_student_record(student):
    if student:
        print("Roll Number:", student["roll_number"])
        print("Name:", student["name"])
        print("Age:", student["age"])
    else:
        print("Student not found!")

# Menu for the program
while True:
    print("\nStudent Records Management")
    print("1. Add Student Record")
    print("2. Search Student Record")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student_record()
        print("Student Record Added!")

    elif choice == "2":
        roll_number = input("Enter Roll Number to search: ")
        student = search_student_record(roll_number)
        display_student_record(student)

    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option (1, 2, or 3).")

# Example Usage:
# - Add student records with option 1.
# - Search for a student record by roll number with option 2.
# - Exit the program with option 3.