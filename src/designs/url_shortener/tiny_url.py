import time
from threading import Lock

from designs.url_shortener.base62 import encode

BASE_URL = "https://short.my/"


class TinyUrlService:
    def __init__(self, limit=100, use_lock=True) -> None:
        self.counter = 1
        self.limit = limit
        self.url_map = {}
        self.reverse_map = {}
        self.use_lock = use_lock
        self.lock = Lock()

    def _sync(self, func):
        if self.use_lock:
            with self.lock:
                return func()
        else:
            return func()

    def shorten_url(self, long_url: str) -> str:
        def op():
            if long_url in self.reverse_map:
                return f"{BASE_URL}{self.reverse_map[long_url]}"

            if self.counter > self.limit:
                raise ValueError("Out of capacity")
            time.sleep(0.001)

            short_url = encode(self.counter)
            self.counter += 1

            self.url_map[short_url] = long_url
            self.reverse_map[long_url] = short_url

            return f"{BASE_URL}{short_url}"

        return self._sync(op)

    def get_long_url(self, short_url: str) -> str:
        short_url = short_url.replace(BASE_URL, "")
        return self.url_map.get(short_url)
