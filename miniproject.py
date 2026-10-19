
# Python Mini Project
# Employee Management System using OOP

class Employee:
    # Constructor to initialize employee details
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    # Method to display employee details
    def display(self):
        print("-" * 40)
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Department  :", self.department)
        print("Salary      : Rs.", format(self.salary, ".2f"))
        print("-" * 40)

    # Method to update employee salary
    def update_salary(self, new_salary):
        self.salary = new_salary
        print("Salary updated successfully!")


# Function to find an employee by ID
def search_employee(employees, emp_id):
    for employee in employees:
        if employee.emp_id == emp_id:
            return employee
    return None


def main():
    employees = []

    while True:
        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Search Employee")
        print("4. Update Employee Salary")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            emp_id = input("Enter Employee ID: ").strip()

            if not emp_id:
                print("Employee ID cannot be empty.")
                continue

            if search_employee(employees, emp_id) is not None:
                print("Employee ID already exists!")
                continue

            name = input("Enter Employee Name: ").strip()
            department = input("Enter Department: ").strip()

            if not name or not department:
                print("Name and department cannot be empty.")
                continue

            try:
                salary = float(input("Enter Salary: "))

                if salary < 0:
                    print("Salary cannot be negative.")
                    continue

            except ValueError:
                print("Please enter a valid numeric salary.")
                continue

            employee = Employee(emp_id, name, department, salary)
            employees.append(employee)
            print("Employee added successfully!")

        elif choice == "2":
            if not employees:
                print("No employee records found.")
            else:
                print("\n===== EMPLOYEE DETAILS =====")
                for employee in employees:
                    employee.display()

        elif choice == "3":
            emp_id = input("Enter Employee ID to search: ").strip()
            employee = search_employee(employees, emp_id)

            if employee is not None:
                print("\nEmployee found!")
                employee.display()
            else:
                print("Employee not found.")

        elif choice == "4":
            emp_id = input("Enter Employee ID: ").strip()
            employee = search_employee(employees, emp_id)

            if employee is not None:
                try:
                    new_salary = float(input("Enter New Salary: "))

                    if new_salary < 0:
                        print("Salary cannot be negative.")
                    else:
                        employee.update_salary(new_salary)

                except ValueError:
                    print("Please enter a valid numeric salary.")
            else:
                print("Employee not found.")

        elif choice == "5":
            emp_id = input("Enter Employee ID to delete: ").strip()
            employee = search_employee(employees, emp_id)

            if employee is not None:
                employees.remove(employee)
                print("Employee deleted successfully!")
            else:
                print("Employee not found.")

        elif choice == "6":
            print("Thank you for using Employee Management System!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 6.")

