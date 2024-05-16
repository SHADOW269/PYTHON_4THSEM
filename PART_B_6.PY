import sqlite3

conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employee
               (empno INTEGER PRIMARY KEY,
               name TEXT,
               salary REAL)''')

def add_employee():
    empno = int(input("Enter employee number: "))
    name = input("Enter employee name: ")
    salary = float(input("Enter employee salary: "))
    cursor.execute("INSERT INTO employee (empno, name, salary) VALUES (?, ?, ?)", (empno, name, salary))
    conn.commit()
    print("Employee added successfully!")

def display_employee():
    empno = int(input("Enter employee number: "))
    cursor.execute("SELECT * FROM employee WHERE empno=?", (empno,))
    employee = cursor.fetchone()
    if employee:
        print("Employee Details:")
        print("Emp Number\t\tEmp Name\t\tSalary")
        print(employee[0], "\t\t\t", employee[1], "\t\t", employee[2])
    else:
        print("Employee not found!")

def display_employee_salary_range():
    min_salary = float(input("Enter minimum salary: "))
    max_salary = float(input("Enter maximum salary: "))
    cursor.execute("SELECT * FROM employee WHERE salary BETWEEN ? AND ?", (min_salary, max_salary))
    employees = cursor.fetchall()
    if employees:
        print("Employees within salary range:")
        print("Emp Number\t\tEmp Name\t\tSalary")
        for employee in employees:
            print(employee[0], "\t\t", employee[1], "\t\t", employee[2])
    else:
        print("No employees found within the salary range!")

def menu():
    while True:
        print("Menu:")
        print("1. Add Employee")
        print("2. Display Employee Details")
        print("3. Display Employees by Salary Range")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employee()
        elif choice == '3':
            display_employee_salary_range()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

menu()
conn.close()
