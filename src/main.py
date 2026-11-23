from models import BankAccount
from exceptions import InvalidOperationError, InsufficientFundsError


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
# пополни счёт, сними часть, выведи get_account_info()

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