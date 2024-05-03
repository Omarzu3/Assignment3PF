from tkinter import messagebox  # Importing messagebox module from tkinter for displaying messages
import pickle  # Importing pickle module for storing data in binary file format

class Employee:
    def __init__(self, name=None, employee_id=None, department=None, job_title=None, basic_salary=None, age=None, date_of_birth=None, passport_details=None, manager_id=None):
        # Constructor for the Employee class
        # Initialize employee attributes
        self.name = name  # Name of the employee
        self.employee_id = employee_id  # Unique id for the employee
        self.department = department  # Department in which the employee works
        self.job_title = job_title  # Job title of the employee
        self.basic_salary = basic_salary  # Basic salary of the employee
        self.age = age  # Age of the employee
        self.date_of_birth = date_of_birth  # Date of birth of the employee
        self.passport_details = passport_details  # Passport details of the employee
        self.manager_id = manager_id  # Manager ID of the employee (if any)
        self.employees = []  # List to store employee data

    def add_employee(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, manager_id=None):
        # Method to add a new employee to the file
        # Create a dictionary with employee details
        employee_data = {
            "name": name,
            "employee_id": employee_id,
            "department": department,
            "job_title": job_title,
            "basic_salary": basic_salary,
            "age": age,
            "date_of_birth": date_of_birth,
            "passport_details": passport_details,
            "manager_id": manager_id
        }
        self.employees.append(employee_data)  # Add employee data to the list

        # Write employee details to a binary file using pickle
        with open("employees.pickle", "wb") as file:
            pickle.dump(self.employees, file)

    def delete_employee(self, employee_id):
        # Method to delete an employee from the file
        # Load employees from the file
        try:
            with open("employees.pickle", "rb") as file:
                employees = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No employees found!")
            return

        # Find and remove the employee with the given ID
        for employee in employees:
            if employee["employee_id"] == employee_id:
                employees.remove(employee)
                break
        else:
            messagebox.showerror("Error", "Employee not found!")
            return

        # Write the updated list of employees back to the file
        with open("employees.pickle", "wb") as file:
            pickle.dump(employees, file)

        messagebox.showinfo("Success", "Employee deleted successfully!")  # Display success message

    def modify_employee(self, employee_id, modified_employee_details):
        # Method to modify details of an existing employee
        # Load employees from the file
        try:
            with open("employees.pickle", "rb") as file:
                employees = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No employees found!")
            return

        # Find the employee with the given ID and modify the details
        for employee in employees:
            if employee["employee_id"] == employee_id:
                employee.update(modified_employee_details)
                break
        else:
            messagebox.showerror("Error", "Employee not found!")
            return

        # Write the updated list of employees back to the file
        with open("employees.pickle", "wb") as file:
            pickle.dump(employees, file)

        messagebox.showinfo("Success", "Employee details modified successfully!")  # Display success message

    @staticmethod
    def display_employee_by_id(employee_id):
        # Static method to display employee details based on the given ID
        # Load employee details from the binary file
        try:
            with open("employees.pickle", "rb") as file:
                employees = pickle.load(file)

            # Find the employee with the given ID
            for employee in employees:
                if employee["employee_id"] == employee_id:
                    return employee

            return None
        except FileNotFoundError:
            messagebox.showerror("Error", "No employees found!")  # Display error message if file not found
            return None
