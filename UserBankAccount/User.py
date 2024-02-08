import bankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email= email
        self.account = bankAccount.BankAccount(int_rate=0.02, balance = 0)


    def deposit(self, amount):
        self.account.deposit(amount)
        return self
    

    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f'{self.name}')
        self.account.desplay_info()
        return self
    
    def balance_with_interest(self):
        print(f'Blance with Interest: {self.account.yeild_interest()}')
        return self

user1 = User('Matt', 'email@email')
user2 = User('Katy', 'kay@email')
user3 = User('Jim', 'jim@email')

user1.deposit(500).display_user_balance()

user2.deposit(1000).withdraw(100).display_user_balance()

user1.balance_with_interest()