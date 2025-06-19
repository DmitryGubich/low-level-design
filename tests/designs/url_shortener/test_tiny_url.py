from concurrent.futures import ThreadPoolExecutor

from designs.url_shortener.tiny_url import TinyUrlService

BASE_URL = "https://short.my/"


def test_tiny_url_service_thread_safety_with_threadpool():
    service = TinyUrlService(limit=10_000, use_lock=True)
    long_url = "https://example.com/very/long/url"
    num_threads = 100

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(service.shorten_url, long_url) for _ in range(num_threads)]
        generated_urls = [future.result() for future in futures]

    # Must be only 1 unique short_url (as we set only one long_url)
    assert len(set(generated_urls)) == 1
