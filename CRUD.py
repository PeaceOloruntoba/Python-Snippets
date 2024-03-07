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
