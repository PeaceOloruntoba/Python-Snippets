class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []
      
    # Create
    def create_employee(self, name, salary):
        emp_id = len(self.employees) + 1
        new_employee = Employee(emp_id, name, salary)
        self.employees.append(new_employee)
        return new_employee
    
    # Read
    def read_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        return None
    
    # Update
    def update_employee(self, emp_id, name, salary):
        emp = self.read_employee(emp_id)
        if emp:
            emp.name = name
            emp.salary = salary
            return emp
        return None

    # Delete
    def delete_employee(self, emp_id):
        emp = self.read_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            return True
        return False


# Example usage
if __name__ == "__main__":
    db = EmployeeDatabase()

    # Create employees
    emp1 = db.create_employee("John Doe", 60000)
    emp2 = db.create_employee("Jane Smith", 70000)

    # Read employee
    read_emp = db.read_employee(emp1.emp_id)
    if read_emp:
        print(f"Employee {read_emp.emp_id}: {read_emp.name}, Salary: ${read_emp.salary}")

    # Update employee
    updated_emp = db.update_employee(emp2.emp_id, "Jane Johnson", 75000)
    if updated_emp:
        print(f"Updated Employee {updated_emp.emp_id}: {updated_emp.name}, Salary: ${updated_emp.salary}")

    # Delete employee
    if db.delete_employee(emp1.emp_id):
        print(f"Employee {emp1.emp_id} deleted")

    # Display remaining employees
    print("Remaining Employees:")
    for emp in db.employees:
        print(f"Employee {emp.emp_id}: {emp.name}, Salary: ${emp.salary}")
