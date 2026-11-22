class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner 
        self.balance = balance
        
        
    def deposit(self, amount): 
        self.amount = amount
        self.balance += amount 
        
        
    def withdraw(self, amount):
        self.amount = amount
        self.balance -= self.amount  
        
    def get_account_info(self):
        return f"Владелец: {self.owner}, баланс: {self.balance}"