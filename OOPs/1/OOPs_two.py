# Ex: create an account class with 2 attributes – balance & account no.
# Create method for debit, credit and printing the balance

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc

    def credit(self, amount):
        self.balance+= amount
        print("Rs.", amount, 'was debited')
        print('the total balance after amount debited is', self.total_balance  ())

    def debit(self, amount):
        self.balance -= amount
        print('the total balance after amount credited is' self.total_balance())

    def total_balance(self):
        return self.balance 


a1 = Account(10000, 98898)
a1.credit(3000)