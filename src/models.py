from exceptions import InvalidOperationError, InsufficientFundsError
class BankAccount:
    def __init__(self, owner, balance=0): 
        if isinstance(balance, bool) or not isinstance(balance, (int,float)):
            raise InvalidOperationError(f"Сумма должна быть числом, получено: {balance!r}")     
        if  balance < 0:
            raise InvalidOperationError(f"Начальный баланс не может быть отрицательным")
        self.owner = owner 
        self.balance = balance 
    
    def _validate_amount(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, (int,float)):
            raise InvalidOperationError(f"Сумма должна быть числом, получено: {amount!r}")
        if amount <= 0:                      
            raise InvalidOperationError(f"Сумма должна быть больше нуля, получено: {amount}")
    
    def deposit(self, amount): 
        self._validate_amount(amount)
        self.balance += amount 
        
    def withdraw(self, amount):
        self._validate_amount(amount)
        if self.balance < amount:
            raise InsufficientFundsError(f"Недостаточно средств: баланс {self.balance}, запрошено {amount}")
        self.balance -= amount  
        
    def get_account_info(self):
        return f"Владелец: {self.owner}, баланс: {self.balance}"
    