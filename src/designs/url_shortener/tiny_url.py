import base64
import random
import re
import string
import threading
from abc import ABC, abstractmethod


class ShorteningStrategy(ABC):
    @abstractmethod
    def generate_short_url(self, long_url):
        pass


class CounterStrategy(ShorteningStrategy):
    def __init__(self):
        self.counter = 1
        self.lock = threading.Lock()

    def generate_short_url(self, long_url):
        with self.lock:
            old_value = self.counter
            self.counter += 1
            return str(old_value)


class Base64Strategy(ShorteningStrategy):
    def generate_short_url(self, long_url):
        return base64.urlsafe_b64encode(long_url.encode()).decode()[:8]


class RandomStrategy(ShorteningStrategy):
    def generate_short_url(self, long_url):
        return "".join(random.choices(string.ascii_letters + string.digits, k=8))


# URL Shortener class
class URLShortener:
    URL_PATTERN = re.compile(r"^(https?://)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*/?$")

    def __init__(self, strategy: ShorteningStrategy):
        self.lock = threading.Lock()
        self.url_map = {}
        self.short_to_url = {}
        self.strategy = strategy

    def shorten(self, long_url):
        if not self._is_valid_url(long_url):
            raise ValueError("Invalid URL format")

        with self.lock:
            if long_url in self.url_map:
                return self.url_map[long_url]
            short_url = self.strategy.generate_short_url(long_url)
            self.url_map[long_url] = short_url
            self.short_to_url[short_url] = long_url
            return short_url

    def unshorten(self, short_url):
        with self.lock:
            return self.short_to_url.get(short_url, None)

    def _is_valid_url(self, url):
        return bool(self.URL_PATTERN.match(url))
