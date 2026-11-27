from exceptions import InvalidOperationError, InsufficientFundsError, AccountFrozenError, AccountClosedError
from enums import AccountStatus, Currency
from abc import ABC, abstractmethod
import uuid

class AbstractAccount(ABC):
    def __init__(self, owner, account_id, balance=0, status=AccountStatus.ACTIVE): 
        self._validate_number(balance)     
        if  balance < 0:
            raise InvalidOperationError(f"Начальный баланс не может быть отрицательным")
        if not isinstance(status, AccountStatus):
            raise  InvalidOperationError(f"Некорректный статус счета: {status}")
        self.owner = owner 
        self._balance = balance 
        self._status = status
        self._account_id = account_id
            
    @property                          
    def balance(self):                
        return self._balance   
        
    @property                          
    def status(self):                
        return self._status
    
    @property 
    def account_id(self):
        return self._account_id
    
    def freeze(self):
        if self._status is AccountStatus.CLOSED:
            raise AccountClosedError("Нельзя заморозить закрытый счёт")
        if self._status is AccountStatus.FROZEN:
            raise AccountFrozenError("Счет уже заморожен")
        self._status = AccountStatus.FROZEN
            
    def unfreeze(self):
        if self._status is AccountStatus.CLOSED:
            raise AccountClosedError("Нельзя разморозить закрытый счёт")
        if self._status is not AccountStatus.FROZEN:
            raise AccountFrozenError(f"Счёт не заморожен, текущий статус: {self._status.value}")
        self._status = AccountStatus.ACTIVE
            
    def close(self):
        if self._status is AccountStatus.CLOSED:
            raise AccountClosedError("Счёт уже закрыт")
        if self._balance > 0:
            raise InvalidOperationError(f"Перед закрытием счета необходимо снять оставшиеся деньги: {self._balance}")
        self._status = AccountStatus.CLOSED
        
    def _validate_number(self, value):
        if isinstance(value, bool) or not isinstance(value, (int,float)):
            raise InvalidOperationError(f"Введенное значение должно быть числом, получено: {value!r}") 
        
    def _check_status(self):
        if self._status is AccountStatus.FROZEN:
            raise AccountFrozenError(f'Статус счёта:{self._status.value}. Обратитесь к администратору')
        if self._status is AccountStatus.CLOSED:
            raise AccountClosedError(f'Статус счёта:{self._status.value}. Счет закрыт, операции над ним невозможны')
            
    def _validate_amount(self, amount):
        self._validate_number(amount)
        if amount <= 0:                      
            raise InvalidOperationError(f"Сумма должна быть больше нуля, получено: {amount}")
    
    @abstractmethod
    def deposit(self, amount):
        """Метод пополнения счета"""
    
    @abstractmethod    
    def withdraw(self, amount):
        """Метод снятия средств со счета"""
        
    @abstractmethod   
    def get_account_info(self):
        """Метод для получения необходимой информации по счету"""
        
        
class BankAccount(AbstractAccount):
    def __init__(self, owner, balance=0, status=AccountStatus.ACTIVE, account_id=None, currency=Currency.RUB):    
        if account_id is None:                      
            account_id = uuid.uuid4().hex[:8]
        
        if not isinstance(currency, Currency):
            raise InvalidOperationError(f"Невозможно открытие счета в данной валюте: {currency}")
        super().__init__(owner, account_id=account_id, balance=balance, status=status)
        self._currency = currency
        
    @property 
    def currency(self):
        return self._currency
        
    def deposit(self, amount): 
        self._check_status() 
        self._validate_amount(amount)
        self._balance += amount 
         
    def withdraw(self, amount):
        self._check_status()
        self._validate_amount(amount)
        if self._balance < amount:
            raise InsufficientFundsError(f"Недостаточно средств: баланс {self._balance}, запрошено {amount}")
        self._balance -= amount  
    
    def get_account_info(self):
        return f"ID счета {self._account_id},статус счета: {self._status.value}, владелец: {self.owner}, баланс: {self._balance} {self._currency.value}"
    
