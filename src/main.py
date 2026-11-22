from models import BankAccount

c1 = BankAccount("Leon", 10)
c2 = BankAccount("Joy", 100)
c1.deposit(100)
c2.withdraw(25)
print(c1.get_account_info())
print(c2.get_account_info())