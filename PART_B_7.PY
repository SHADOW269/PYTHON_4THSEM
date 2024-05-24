import sqlite3

conn = sqlite3.connect('customer.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS electricity_bill (
    TariffCode TEXT,
    Customer_Name TEXT,
    Meter_Number INTEGER PRIMARY KEY,
    Previous_Reading INTEGER,
    Current_Reading INTEGER
)''')

def add_customer():
    Tariff_code = input("Enter TariffCode: ")
    Cust_name = input("Enter customer name: ")
    Meter_no = int(input("Enter Meter Number: "))
    prev_read = 0
    curr_read = -1
    while prev_read > curr_read:
        print("Previous reading must be less than current reading")
        prev_read = int(input("Enter previous reading: "))
        curr_read = int(input("Enter current reading: "))
    cursor.execute('''INSERT INTO electricity_bill VALUES (?, ?, ?, ?, ?)''',
                   (Tariff_code, Cust_name, Meter_no, prev_read, curr_read))
    conn.commit()
    print("Customer added successfully!")

def display_customer():
    cursor.execute("SELECT * FROM electricity_bill")
    customers = cursor.fetchall()
    print("Customer details:")
    print("TariffCode\tCustomer_Name\tMeter_Number\tPrevious_Reading\tCurrent_Reading")
    for customer in customers:
        print(customer[0], "\t", customer[1], "\t", customer[2], "\t\t", customer[3], "\t\t", customer[4])

def update_customer():
    meter_no = int(input("Enter Meter Number: "))
    previous_reading = int(input("Enter previous reading: "))
    current_reading = int(input("Enter current reading: "))
    cursor.execute('''UPDATE electricity_bill SET Previous_Reading=?, Current_Reading=? WHERE Meter_Number=?''',
                   (previous_reading, current_reading, meter_no))
    conn.commit()
    display_customer()

def calculate_bill_amt(Meter_No):
    cursor.execute('''SELECT * FROM electricity_bill WHERE Meter_Number=?''', (Meter_No,))
    result = cursor.fetchone()
    if result:
        print("Customer Details:")
        print("-------------------------------")
        print("TariffCode: ", result[0])
        print("Customer-Name : ", result[1])
        print("Previous-Reading: ", result[3])
        print("Current-Reading: ", result[4])
        if result[3] is None or result[4] is None:
            print("Previous and current readings not updated")
            return
        units_consumed = result[4] - result[3]
        print("Units-Consumed: ", units_consumed)
        bill_amt = 0
        if result[0] == 'LT1':
            if units_consumed >= 0 and units_consumed <= 30:
                bill_amt = units_consumed * 2
            elif units_consumed >= 31 and units_consumed <= 100:
                bill_amt = units_consumed * 3.5
            elif units_consumed >= 101 and units_consumed <= 200:
                bill_amt = units_consumed * 4.5
            elif units_consumed > 200:
                bill_amt = units_consumed * 5
        elif result[0] == 'LT2':
            if units_consumed >= 0 and units_consumed <= 30:
                bill_amt = units_consumed * 3.5
            elif units_consumed >= 31 and units_consumed <= 100:
                bill_amt = units_consumed * 5.0
            elif units_consumed >= 101 and units_consumed <= 200:
                bill_amt = units_consumed * 6.0
            elif units_consumed > 200:
                bill_amt = units_consumed * 7.5
        print("Bill-Amount: Rs. ", bill_amt)

def menu():
    while True:
        print("Menu:")
        print("1. Add Customer Details")
        print("2. Display Customer Details")
        print("3. Update Customer Details by meter number")
        print("4. Electricity Bill")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_customer()
        elif choice == '2':
            display_customer()
        elif choice == '3':
            update_customer()
        elif choice == '4':
            meterno = int(input("Enter meter number to get bill: "))
            calculate_bill_amt(meterno)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

menu()

conn.close()
