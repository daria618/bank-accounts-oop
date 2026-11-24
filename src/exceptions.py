class AccountError(Exception):
    pass


class AccountFrozenError(AccountError):
    """Некорректная операция: счет заморожен."""


class AccountClosedError(AccountError):
    """Некорректная операция: счет закрыт."""


class InvalidOperationError(AccountError):
    """Некорректная операция: неверная сумма или тип данных."""
    
class InsufficientFundsError(AccountError):
    """На балансе недостаточно средств для снятия."""