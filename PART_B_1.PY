class Employee:
    def __init__(self, empno, name, depname, designation, age, salary):
        self.empno = empno
        self.name = name
        self.depname = depname
        self.designation = designation
        self.age = age
        self.salary = salary
class EmployeeDB:
    def __init__(self):
        self.emp_list = []
    def add_employee(self, emp):
        self.emp_list.append(emp)
    def search_employee(self, empno):
        for emp in self.emp_list:
            if emp.empno == empno:
                return emp
        return None
    def display_all(self):
        for emp in self.emp_list:
            print(emp.empno," | ",emp.name," | ",emp.depname," | ",emp.designation," | ",emp.age," | ",emp.salary)
emp_db = EmployeeDB()
choice=1
while choice >= 1 and choice <= 3:
    print("__________employee details__________")
    print("1)Add employee details")
    print("2)search an employee based on salary")
    print("3)display employee details")
    print("4)exit")
    print("--------------------------------------------")
    choice = int(input("Enter the choice:"))
    if (choice == 1):
        n = int(input("Enter the number of employees: "))
        for i in range(n):
            empno = int(input("Enter Employee No: "))
            name = input("Enter Employee Name: ")
            depname = input("Enter Department Name: ")
            designation = input("Enter Designation: ")
            age = int(input("Enter Age: "))
            salary = float(input("Enter Salary: "))
            emp = Employee(empno, name, depname, designation, age, salary)
            emp_db.add_employee(emp)
    elif (choice == 2):
        empno = int(input("Enter Employee No to search: "))
        emp = emp_db.search_employee(empno)
        if emp:
            print("Employee Found:")
            print("Emp No:", emp.empno)
            print("Name:", emp.name)
            print("Department Name:", emp.depname)
            print("Designation:", emp.designation)
            print("Age:", emp.age)
            print("Salary:", emp.salary)
        else:
            print("Employee not found")
    elif (choice == 3):
        print("\n")
        print("EMPNO | EMPNAME |DEPARTMENT NAME | DESIGNATION | AGE | SALARY")
        emp_db.display_all()
    elif (choice == 4):
        exit(0)