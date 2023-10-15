class Employee:
    def __init__(self, emp_id, name, designation):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation

    def calculate_earnings(self):
        pass

    def display(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")

class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, salary):
        super().__init__(emp_id, name, "Full-Time")
        self.salary = salary

    def calculate_earnings(self):
        return self.salary

    def display(self):
        super().display()
        print(f"Salary: ${self.salary}")

class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name, "Part-Time")
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_earnings(self):
        return self.hourly_rate * self.hours_worked

    def display(self):
        super().display()
        print(f"Hourly Rate: ${self.hourly_rate}")
        print(f"Hours Worked: {self.hours_worked}")
        print(f"Earnings: ${self.calculate_earnings()}")

# Main program
employees = []

while True:
    print("\nEmployee Management System")
    print("1. Add Full-Time Employee")
    print("2. Add Part-Time Employee")
    print("3. Display Employee Details")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        salary = float(input("Enter Salary: "))
        full_time_employee = FullTimeEmployee(emp_id, name, salary)
        employees.append(full_time_employee)
        print("Full-Time Employee added!")

    elif choice == "2":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        hourly_rate = float(input("Enter Hourly Rate: "))
        hours_worked = float(input("Enter Hours Worked: "))
        part_time_employee = PartTimeEmployee(emp_id, name, hourly_rate, hours_worked)
        employees.append(part_time_employee)
        print("Part-Time Employee added!")

    elif choice == "3":
        for employee in employees:
            employee.display()
            print()

    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option (1, 2, 3, or 4).")