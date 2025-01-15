class BankAccount:
    def __init__(self,initial_balance=0):
        self.balance=initial_balance
         
    def deposit(self,amount):
        if amount>0:
            self.balance=balance+amount
            print('Deposited {amount}')
        else:
            print('-v')
    def withdraw(self,amount):
        if amout<self.balance:
            self.balance=self.balance-amount
            #remaining logic
            
    def get_balance(self):
        return self.balance

    
account=BankAccount()
account.deposit(100)
account.get_balance()
account.withdraw(50)
