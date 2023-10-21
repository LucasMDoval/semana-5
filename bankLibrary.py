class account:
    def __init__(self, number, balance = 0):
        self.number = number
        self.balance = balance
    
    def get_number (self):
        return self.number
    
    def deposit (self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def get_balance (self,):
        return self.balance

account1 = account("ES9999999999999999", 1000)


account1.deposit(100)
account1.withdraw(5000)


if account1.get_balance() > 0 :
    print (f"A la cuenta con el numero {account1.get_number()} le quedan {account1.get_balance()}$")
else:
    print (f"La cuenta con número {account1.get_number()} debe {abs(account1.get_balance())}$")


