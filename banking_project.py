# Banking system using OOP 

# Parent class: User
# Holds details about the user
# Has a function to show user details

# Child class: Bank
# Stores details about the account balance
# Stores details about the amount
# Allows deposits, withdraw and view balance

# Parent class
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details ->")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


# Child class
class BankAcc(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, d_amount):
        self.d_amount = d_amount
        self.balance = self.balance + self.d_amount
        print(f"Deposit of ${self.d_amount} successful")
        print(f"Updated account balance: ${self.balance}")

    def withdraw(self, w_amount):
        self.w_amount = w_amount
        if (self.w_amount > self.balance):
            print(f"Withdrawal of ${self.w_amount} denied due to insufficient funds")
            print(f"Current available balance: ${self.balance}")
        else:
            self.balance = self.balance - self.w_amount
            print(f"Withdrawal of ${self.w_amount} successful")
            print(f"Updated account balance: ${self.balance}")

    def view_balance(self):
        print("Hello,", self.name)
        print(f"Your account balance is: ${self.balance}")

viththal = BankAcc("Viththal",23,"Male")

viththal.show_details()
viththal.deposit(1000)
viththal.withdraw(400)
viththal.withdraw(2000)
viththal.view_balance()