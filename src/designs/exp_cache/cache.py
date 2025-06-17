import threading
import time
from datetime import datetime


def now():
    return datetime.now().strftime("%H:%M:%S.%f")[:-3]


class AutoExpiringCache:
    def __init__(self, default_ttl):
        self.cache = {}
        self.ttl = default_ttl
        self.lock = threading.Lock()

    def set(self, key, value, ttl=None):
        expire_at = time.time() + (ttl if ttl is not None else self.ttl)
        with self.lock:
            self.cache[key] = (value, expire_at)
            print(
                f"[{now()}] [CACHE] Set {key} = {value}, expires in {expire_at - time.time():.1f}s"
            )

    def get(self, key):
        with self.lock:
            if key in self.cache:
                value, expire_at = self.cache[key]
                if time.time() < expire_at:
                    print(f"[{now()}] [CACHE] Get {key} = {value}")
                    return value
                else:
                    print(f"[{now()}] [CACHE] Get {key} expired — deleting")
                    del self.cache[key]
            else:
                print(f"[{now()}] [CACHE] Get {key} — not found")
        return None

    def delete(self, key):
        with self.lock:
            if key in self.cache:
                del self.cache[key]
                print(f"[{now()}] [CACHE] Deleted {key}")

    def cleanup(self):
        now = time.time()
        with self.lock:
            ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            keys_to_delete = [k for k, v in self.cache.items() if v[1] < now]
            for key in keys_to_delete:
                print(f"[{ts}] [CLEANUP] Deleted expired key: {key}")
                del self.cache[key]

    def autoclean(self, interval=30):
        def loop():
            while True:
                time.sleep(interval)
                self.cleanup()

        thread = threading.Thread(target=loop, daemon=True)
        thread.start()
