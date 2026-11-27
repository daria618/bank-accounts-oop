from models import BankAccount, AbstractAccount
from exceptions import InvalidOperationError, InsufficientFundsError, AccountFrozenError, AccountClosedError
from enums import AccountStatus, Currency

c1 = BankAccount("Leon", 100)

print("--- Сценарий: снять больше, чем есть на счёте ---")
try:
    c1.withdraw(500)
except InsufficientFundsError as e:
    print(f"Ошибка: {e}")
print(c1.get_account_info())

print("--- Сценарий: успешные операции ---")
c1.deposit(19990)
c1.withdraw(1000)
print(c1.get_account_info())

print("--- Сценарий: пополнение на отрицательную сумму ---")
try:
    c1.deposit(-322)
except InvalidOperationError as e:
    print(f"Ошибка: {e}")

print("--- Сценарий: пополнение строкой '100' ---")
try:
    c1.deposit('100')
except InvalidOperationError as e:
    print(f"Ошибка: {e}")

print("--- Сценарий: пополнение на True ---")
try:
    c1.deposit(True)
except InvalidOperationError as e:
    print(f"Ошибка: {e}")

print("--- Сценарий: счёт с отрицательным начальным балансом ---")
try:
    bad = BankAccount("Dasha", -2000)
except InvalidOperationError as e:
    print(f"Ошибка: {e}")

print("--- Сценарий: создать замороженный счёт и попробовать пополнить ---")
try:
    c_frozen = BankAccount("Dasha", 2000, status=AccountStatus.FROZEN)
    c_frozen.deposit(1000)
except AccountFrozenError as e:
    print(f"Ошибка: {e}")
    
print("--- Сценарий: закрыть → попробовать снять → AccountClosedError ---")
try:
    c_closed = BankAccount("Dasha")
    c_closed.close()
    c_closed.withdraw(100)
except AccountClosedError as e:
    print(f"Ошибка: {e}")
    
print("--- Сценарий: разморозить → успешная операция ---")
try:
    c_active = BankAccount("Dasha", 2000)
    c_active.freeze()
    c_active.unfreeze()
    c_active.deposit(1000000)
except AccountFrozenError as e:
    print(f"Ошибка: {e}")
print(c_active.get_account_info())

print("--- Сценарий: попытка изменить баланс напрямую ---")
c_invalid = BankAccount("Dasha", 2000)
try:
    c_invalid.balance = 1_000_000
except AttributeError as e:
    print("Используйте правильный метод для изменения баланса")
print(c_invalid.get_account_info())

print("--- Сценарий: попытка создать AbstractAccount ---")
try:
    c = AbstractAccount("Test")
except TypeError as e:
    print(e)

print("--- Сценарий: проверка генерации account_id ---")
acc1 = BankAccount("Tom", 1000, currency=Currency.RUB)
acc1b = BankAccount("TomB", 1000, currency=Currency.RUB)
print(acc1.account_id != acc1b.account_id)

print("--- Сценарий: счёт с явным account_id='ACC-0001' ---")
acc2 = BankAccount("Tom", 1600,  account_id='ACC-0001', currency=Currency.USD)
print(acc2.get_account_info())

print("--- Сценарий: неверная валюта: currency='USD' ---")
try:
    acc3 = BankAccount("Tortm", 1600, currency='USD')
except InvalidOperationError as e:
    print("Неверно введена Валюта счета")