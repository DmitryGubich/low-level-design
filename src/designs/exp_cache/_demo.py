import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from random import randint

from designs.exp_cache.cache import AutoExpiringCache

if __name__ == "__main__":
    cache = AutoExpiringCache(default_ttl=5)
    cache.autoclean(interval=2)

    def now():
        return datetime.now().strftime("%H:%M:%S.%f")[:-3]

    def writer(thread_id):
        for i in range(5):
            key = f"key_{i}"
            value = f"writer-{thread_id}-{i}"
            cache.set(key, value)
            time.sleep(randint(1, 3) * 0.1)

    def reader(thread_id):
        for i in range(5):
            key = f"key_{i}"
            cache.get(key)
            time.sleep(randint(1, 3) * 0.1)

    with ThreadPoolExecutor(max_workers=6) as executor:
        for i in range(3):
            executor.submit(writer, i)
            executor.submit(reader, i)

    print(f"[{now()}] All thread are finished.")
