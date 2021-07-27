class Employee:
    emp_name = 'Ram'

    def empName(self):
        print(self.emp_name)
Employee.empName=classmethod(Employee.empName)
Employee.empName()