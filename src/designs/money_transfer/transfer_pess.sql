CREATE TABLE accounts (
    account_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    balance NUMERIC(18,2) NOT NULL CHECK (balance >= 0),
    version INTEGER NOT NULL DEFAULT 0
);

BEGIN;

-- Захватываем блокировки строк для обеих учётных записей
SELECT balance FROM accounts WHERE account_id = 1 FOR UPDATE;
SELECT balance FROM accounts WHERE account_id = 2 FOR UPDATE;

DO $$
DECLARE
    sender_balance NUMERIC(18,2);
BEGIN
    -- Получаем баланс отправителя
    SELECT balance INTO sender_balance FROM accounts WHERE account_id = 1;

    -- Проверяем баланс
    IF sender_balance < 100 THEN
        RAISE EXCEPTION 'Insufficient Balance';
    END IF;

    -- Списываем и зачисляем деньги
    UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
    UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;
END $$;

COMMIT;
