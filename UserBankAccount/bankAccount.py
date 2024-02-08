
class BankAccount:
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        self.balance -= amount 

    def desplay_info(self):
        print("===========")
        print(f'Balance: {self.balance}')
        print(f'Interest Rate: {self.int_rate}')
        print(f'Balance w/ Interest: {self.yeild_interest()}')
        print("===========")

    def yeild_interest(self):
        self.balance += (self.balance * self.int_rate)
