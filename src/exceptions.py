class AccountError(Exception):
    pass


class AccountFrozenError(AccountError):
    pass


class AccountClosedError(AccountError):
    pass


class InvalidOperationError(AccountError):
    """Некорректная операция: неверная сумма или тип данных."""
    
    
class InsufficientFundsError(AccountError):
    """На балансе недостаточно средств для снятия."""