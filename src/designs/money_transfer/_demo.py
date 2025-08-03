import threading
from decimal import Decimal
from time import time

from src.designs.money_transfer.transfer import Account, Transfer


def test_concurrent_transfers():
    acc1 = Account(account_id=1, balance=1000)
    acc2 = Account(account_id=2, balance=1000)
    initial_total = acc1.get_balance() + acc2.get_balance()

    def transfer():
        Transfer.transfer_money(from_account=acc1, to_account=acc2, amount=Decimal(-50))

    threads = [threading.Thread(target=transfer) for _ in range(5)]
    start_time = time()

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time()
    final_total = acc1.get_balance() + acc2.get_balance()

    assert final_total == initial_total, "Total balance should remain constant"
    assert (end_time - start_time) < 5, "Potential deadlock detected"
