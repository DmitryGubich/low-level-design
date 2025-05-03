import time
from threading import Lock

from designs.url_shortener.base62 import encode

BASE_URL = "https://short.my/"


class TinyUrlService:
    def __init__(self, limit=100) -> None:
        self.counter = 1
        self.limit = limit
        self.url_map = {}
        self.reverse_map = {}
        self.lock = Lock()

    def shorten_url(self, long_url: str) -> str:
        if long_url in self.reverse_map:
            self.reverse_map.get(long_url)
        short_url = encode(self.counter)

        with self.lock:
            self._increase_counter()
        self.url_map[short_url] = long_url
        self.reverse_map[long_url] = short_url
        return f"{BASE_URL}{short_url}"

    def get_long_url(self, short_url: str) -> str:
        short_url = short_url.replace(BASE_URL, "")
        return self.url_map.get(short_url)

    def _increase_counter(self) -> None:
        if self.counter > self.limit:
            raise ValueError("Out of capacity")
        time.sleep(0.001)
        self.counter += 1
