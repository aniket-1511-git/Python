'''Scenario:
Simulate a simple bank system: create accounts, deposit, withdraw, and check balances.

What you’ll learn:
Using classes for real-life simulations
Method design and data encapsulation

Task:
Log Session a BankAccount class with methods for deposit, withdraw, and balance check.

Example:
Start with balance 1000, deposit 500, withdraw 300, show balance.

Expected Output:
1200'''
class BankAccount:
    def __init__(self):
        self.amount=1000
    def deposit(self):
        print("enter Amount to deposit")
        a=int(input())
        self.amount=self.amount + a
    def withdraw(self):
        print("enter Amount to withdraw")
        a = int(input())
        if self.amount >0 and a>self.amount:
            self.amount-=a
    def total_balance(self):
        print(self.amount)
    
u1= BankAccount()
while 1:
    print("1.deposit 2.withdraw 3.total_balance ")
    op=int(input())
    match op:
        case 1:
            u1.deposit()
        case 2:
            u1.withdraw()
        case 3:
            u1.total_balance()
    