BEGIN;

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

DO $$
DECLARE
    sender_balance NUMERIC(18,2);
BEGIN
    SELECT balance INTO sender_balance FROM accounts WHERE account_id = 1;

    IF sender_balance < 100 THEN
        RAISE EXCEPTION 'Insufficient funds';
    END IF;

    UPDATE accounts
    SET balance = balance - 100
    WHERE account_id = 1;

    UPDATE accounts
    SET balance = balance + 100
    WHERE account_id = 2;
END $$;

COMMIT;