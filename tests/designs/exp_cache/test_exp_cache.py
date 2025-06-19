import random
import threading

from designs.exp_cache.cache import AutoExpiringCache


def test_cache_thread_safety():
    cache = AutoExpiringCache(default_ttl=5, use_lock=True)

    def writer():
        for i in range(500):
            key = f"key_{i % 100}"
            cache.set(key, i)

    def reader():
        for _ in range(500):
            key = f"key_{random.randint(0, 99)}"
            _ = cache.get(key)

    def deleter():
        for _ in range(500):
            key = f"key_{random.randint(0, 99)}"
            cache.delete(key)

    def iterator():
        for _ in range(200):
            for _ in cache.cache:
                pass

    threads = []
    for _ in range(4):
        threads.extend(
            [
                threading.Thread(target=writer),
                threading.Thread(target=reader),
                threading.Thread(target=deleter),
                threading.Thread(target=iterator),
            ]
        )

    for t in threads:
        t.start()
    for t in threads:
        t.join()
