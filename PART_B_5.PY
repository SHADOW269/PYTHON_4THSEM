import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS student (
               regno INTEGER PRIMARY KEY,
               name TEXT,
               subject1 INTEGER,
               subject2 INTEGER,
               subject3 INTEGER
               )''')

def add_student():
    regno = int(input("Enter registration number: "))
    name = input("Enter name: ")
    subject1 = int(input("Enter marks for subject 1: "))
    subject2 = int(input("Enter marks for subject 2: "))
    subject3 = int(input("Enter marks for subject 3: "))

    cursor.execute('''INSERT INTO student (regno, name, subject1, subject2, subject3)
                    VALUES (?, ?, ?, ?, ?)''', (regno, name, subject1, subject2, subject3))
    conn.commit()
    print("Student details added successfully.")

def display_students():
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    print("Student details:")
    print("Reg No\tName\tSubject 1\tSubject 2\tSubject 3")
    for student in students:
        print(student[0], "\t", student[1], "\t", student[2], "\t\t", student[3], "\t\t", student[4])

def delete_student(regno):
    cursor.execute("DELETE FROM student WHERE regno=?", (regno,))
    conn.commit()
    print("Student record deleted successfully.")

while True:
    print("\n--- Student Database Management ---")
    print("1. Add Student") 
    print("2. Display Students")
    print("3. Delete Student")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        regno = int(input("Enter registration number of student to delete: "))
        delete_student(regno)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")

conn.close()
