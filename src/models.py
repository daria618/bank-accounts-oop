from exceptions import InvalidOperationError, InsufficientFundsError, AccountFrozenError, AccountClosedError
from enums import AccountStatus
class BankAccount:
    def __init__(self, owner, balance=0, status=AccountStatus.ACTIVE): 
        if isinstance(balance, bool) or not isinstance(balance, (int,float)):
            raise InvalidOperationError(f"Сумма должна быть числом, получено: {balance!r}")     
        if  balance < 0:
            raise InvalidOperationError(f"Начальный баланс не может быть отрицательным")
        if not isinstance(status, AccountStatus):
            raise  InvalidOperationError(f"Некорректный статус счета: {status}")
        self.owner = owner 
        self.balance = balance 
        self.status = status
    
    def deposit(self, amount): 
        self._check_status() 
        self._validate_amount(amount)
        self.balance += amount 
        
    def withdraw(self, amount):
        self._check_status()
        self._validate_amount(amount)
        if self.balance < amount:
            raise InsufficientFundsError(f"Недостаточно средств: баланс {self.balance}, запрошено {amount}")
        self.balance -= amount  
    
    def get_account_info(self):
        return f"Статус счета: {self.status.value}, владелец: {self.owner}, баланс: {self.balance}"
    
    def freeze(self):
        if self.status is AccountStatus.CLOSED:
            raise AccountClosedError("Нельзя заморозить закрытый счёт")
        if self.status is AccountStatus.FROZEN:
            raise AccountFrozenError("Счет уже заморожен")
        self.status = AccountStatus.FROZEN
        
    def unfreeze(self):
        if self.status is AccountStatus.CLOSED:
            raise AccountClosedError("Нельзя разморозить закрытый счёт")
        if self.status is not AccountStatus.FROZEN:
            raise InvalidOperationError(f"Счёт не заморожен, текущий статус: {self.status.value}")
        self.status = AccountStatus.ACTIVE
        
    def close(self):
        if self.status is AccountStatus.CLOSED:
            raise AccountClosedError("Счёт уже закрыт")
        if self.balance > 0:
            raise InvalidOperationError(f"Перед закрытием счета необходимо снять оставшиеся деньги: {self.balance}")
        self.status = AccountStatus.CLOSED
    
    def _check_status(self):
        if self.status is AccountStatus.FROZEN:
            raise AccountFrozenError(f'Статус счёта:{self.status.value}. Обратитесь к админиcтратору')
        if self.status is AccountStatus.CLOSED:
            raise AccountClosedError(f'Статус счёта:{self.status.value}. Счет закрыт, операции над ним невозможны')
        
    def _validate_amount(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, (int,float)):
            raise InvalidOperationError(f"Сумма должна быть числом, получено: {amount!r}")
        if amount <= 0:                      
            raise InvalidOperationError(f"Сумма должна быть больше нуля, получено: {amount}")