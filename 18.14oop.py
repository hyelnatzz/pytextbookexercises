class Account:
    num_of_acct = 0
    @classmethod
    def add_account(cls):
        cls.num_of_acct += 1

    
    def __init__(self, acct_num, name, opening_balance, acct_type):
        Account.add_account()
        self.acct_num = acct_num
        self.name = name
        self.balance = opening_balance
        self.acct_type = acct_type
        print('Number of Account instances created:', Account.num_of_acct)
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f'Account[{self.acct_num}] - {self.name}, {self.acct_type} account = {self.balance}'
    
    


acc1 = Account('123', 'John', 10.05, 'current')
"""acc2 = Account('345', 'John', 23.55, 'savings')
acc3 = Account('567', 'Phoebe', 12.45, 'investment')
print(acc1)
print(acc2)
print(acc3)
acc1.deposit(23.45)
acc1.withdraw(12.33)
print('balance:', acc1.get_balance())"""


