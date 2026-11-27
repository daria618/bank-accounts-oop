class AccountError(Exception):
    """Базовое исключение для всех ошибок счёта."""


class AccountFrozenError(AccountError):
    """Некорректная операция: счет заморожен."""


class AccountClosedError(AccountError):
    """Некорректная операция: счет закрыт."""


class InvalidOperationError(AccountError):
    """Некорректная операция: неверная сумма или тип данных."""
    
class InsufficientFundsError(AccountError):
    """На балансе недостаточно средств для снятия."""
    
