class BankAccount:
    def __init__(self, owner, balance=1):
        self.owner = owner
        self.balance = balance

    def view_balance(self):
        print(self.balance)

    def deposit(self):
        amount = int(input("Enter the amount to be deposited: "))
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Enter a valid amount!")

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw: "))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Enter a valid amount or check your balance!")

# Create a bank account object
owner = input("Enter the account owner's name: ")
account = BankAccount(owner)

while True:
    print("\nSelect an option:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        account.view_balance()
    elif choice == 2:
        account.deposit()
    elif choice == 3:
        account.withdraw()
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please select again.")
