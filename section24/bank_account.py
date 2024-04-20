class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, balance):
        self.balance += balance
        return self.balance

    def withdraw(self, balance):
        self.balance -= balance
        return self.balance
