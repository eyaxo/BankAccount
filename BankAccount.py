class BankAccount:
    def __init__(self, interestRate, balance):
        self.interestRate = interestRate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount 
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        return print('balance', '=', self.balance)

    def yeild_interest(self):
        self.balance *= self.interestRate
        return self

accountOne = BankAccount(2.1, 200)   
accountTwo = BankAccount(2.1, 165)

accountOne.deposit(5).deposit(10).deposit(15).withdraw(3).yeild_interest().display_account_info()
accountTwo.deposit(1).deposit(4).withdraw(10).withdraw(2).withdraw(1).withdraw(20).yeild_interest().display_account_info()

