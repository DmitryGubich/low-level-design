import threading
import time


class AutoExpiringCache:
    def __init__(self, default_ttl=60, use_lock=True):
        self.cache = {}
        self.ttl = default_ttl
        self.use_lock = use_lock
        self.lock = threading.Lock()

    def _sync(self, func):
        if self.use_lock:
            with self.lock:
                return func()
        else:
            return func()

    def set(self, key, value, ttl=None):
        def op():
            expire_at = time.time() + (ttl if ttl is not None else self.ttl)
            self.cache[key] = (value, expire_at)

        self._sync(op)

    def get(self, key):
        def op():
            if key in self.cache:
                value, expire_at = self.cache[key]
                time.sleep(0.001)
                if time.time() < expire_at:
                    return value
                else:
                    del self.cache[key]
            return None

        return self._sync(op)

    def delete(self, key):
        def op():
            if key in self.cache:
                time.sleep(0.001)
                del self.cache[key]

        self._sync(op)

    def cleanup(self):
        def op():
            now_ts = time.time()
            keys_to_delete = [k for k, (_, exp) in self.cache.items() if exp < now_ts]
            time.sleep(0.001)
            for k in keys_to_delete:
                del self.cache[k]

        self._sync(op)

    def autoclean(self, interval=30):
        def loop():
            while True:
                time.sleep(interval)
                self.cleanup()

        thread = threading.Thread(target=loop, daemon=True)
        thread.start()
