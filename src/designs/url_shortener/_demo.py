from unittest.mock import patch

import pytest

from designs.url_shortener.tiny_url import (
    URLShortener,
    CounterStrategy,
    Base64Strategy,
    RandomStrategy,
)


@pytest.fixture
def test_urls():
    return ["https://example.com", "https://test.com/page1", "https://another-example.org/about"]


def test_counter_strategy_uniqueness(test_urls: list[str]):
    shortener = URLShortener(CounterStrategy())
    short_urls = {shortener.shorten(url) for url in test_urls}

    assert len(short_urls) == len(test_urls)


def test_base64_strategy_valid_length(test_urls: list[str]):
    shortener = URLShortener(Base64Strategy())
    short_urls = [shortener.shorten(url) for url in test_urls]

    for short_url in short_urls:
        assert 1 <= len(short_url) <= 8


def test_unshorten_correctness(test_urls: list[str]):
    shortener = URLShortener(CounterStrategy())
    mapping = {url: shortener.shorten(url) for url in test_urls}

    for url, short in mapping.items():
        assert shortener.unshorten(short) == url


def test_random_strategy_correctness(test_urls: list[str]):
    shortener = URLShortener(RandomStrategy())
    short_urls = {shortener.shorten(url) for url in test_urls}

    assert len(short_urls) == len(test_urls)


def test_random_strategy_mock_correctness(test_urls: list[str]):
    shortener = URLShortener(RandomStrategy())

    sequence = ["agfhyjko", "cvbgrugd", "asweryi7"]

    with patch("src.designs.url_shortener.tiny_url.random.choices", side_effect=sequence):
        results = [shortener.shorten(url) for url in test_urls]

    expected = sequence
    assert results == expected


def test_invalid_url_handling():
    shortener = URLShortener(CounterStrategy())

    with pytest.raises(ValueError):
        shortener.shorten("invalid-url")
