class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount. Amount must be greater than 0."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}"

# Create an instance of the BankAccount class
my_account = BankAccount("12345", "John Doe", 1000.0)

# Test deposit and withdrawal functionality
print(my_account.display_balance())  # Display initial balance
print(my_account.deposit(500))  # Deposit $500
print(my_account.withdraw(200))  # Withdraw $200
print(my_account.display_balance())  # Display updated balance
