import threading
from decimal import Decimal


class Account:
    def __init__(self, account_id, balance=Decimal(0)):
        self.account_id = account_id
        self.balance = balance
        self.lock = threading.RLock()

    def deposit(self, amount):
        self._validate_amount(amount=amount)
        with self.lock:
            self.balance += amount

    def withdraw(self, amount: Decimal):
        self._validate_amount(amount=amount)
        with self.lock:
            if self.get_balance() >= amount:
                self.balance -= amount
                return True
            raise InsufficientFundsException("Not enough funds")

    def get_balance(self):
        with self.lock:
            return self.balance

    def _validate_amount(self, amount: Decimal) -> None:
        if amount <= 0:
            raise WrongAmountException("Amount must be greater than 0")


class Transfer:
    @staticmethod
    def transfer_money(from_account: Account, to_account: Account, amount: Decimal) -> bool:
        if from_account.account_id < to_account.account_id:
            first, second = from_account, to_account
        else:
            first, second = to_account, from_account

        with first.lock, second.lock:
            if from_account.withdraw(amount):
                to_account.deposit(amount)
                print(f"Successful transfer {amount} | {from_account} → {to_account}")
                return True
            return False


class InsufficientFundsException(Exception):
    pass


class WrongAmountException(Exception):
    pass
