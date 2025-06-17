import threading

import pytest

from src.designs.exp_cache.cache import AutoExpiringCache


@pytest.mark.repeat(24)
def test_thread_safety():
    cache = AutoExpiringCache(default_ttl=1)
    errors = []

    def worker():
        try:
            for i in range(1000):
                key = f"key_{i % 10}"
                cache.set(key, i)
                val = cache.get(key)
                if val is not None and not isinstance(val, int):
                    errors.append(f"Invalid value: {val}")
        except Exception as e:
            errors.append(str(e))

    threads = [threading.Thread(target=worker) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert not errors, f"Errors occurred: {errors}"
