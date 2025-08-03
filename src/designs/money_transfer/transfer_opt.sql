BEGIN;

DO $$
DECLARE
    rows_affected INT;
BEGIN
    -- Попытка списания с учётом версии и достаточного баланса
    UPDATE accounts
    SET balance = balance - 100, version = version + 1
    WHERE account_id = 1
      AND balance >= 100
      AND version = (SELECT version FROM accounts WHERE account_id = 1);

    GET DIAGNOSTICS rows_affected = ROW_COUNT;
    IF rows_affected = 0 THEN
        RAISE EXCEPTION 'Optimistic Locking Failed: Balance too low or version mismatch on sender';
    END IF;

    -- Попытка зачисления с учётом версии
    UPDATE accounts
    SET balance = balance + 100, version = version + 1
    WHERE account_id = 2
      AND version = (SELECT version FROM accounts WHERE account_id = 2);

    GET DIAGNOSTICS rows_affected = ROW_COUNT;
    IF rows_affected = 0 THEN
        RAISE EXCEPTION 'Optimistic Locking Failed: Version mismatch on receiver';
    END IF;
END $$;

COMMIT;