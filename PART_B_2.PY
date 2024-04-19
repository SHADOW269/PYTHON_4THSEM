class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient Balance.")
    def get_balance(self):
        return self.balance
class SavingsAccount (BankAccount):
    def __init__(self, interest_rate):
        super().__init__()
        self.interest_rate = interest_rate
    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} added to the account.")
account=SavingsAccount(interest_rate=0.05)
while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Get Balance")
    print("4. Calculate Interest")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = float(input("Enter The Amount to deposit: "))
        account.deposit(amount)
    elif choice == 2:
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
    elif choice == 3:
        balance = account.get_balance()
        print(f"Current balance:{balance} ")
    elif choice == 4:
        account.calculate_interest()
    elif choice == 5:
        print("Exiting the program.")
    else:
        print("Invalid choice. PLease try again.")