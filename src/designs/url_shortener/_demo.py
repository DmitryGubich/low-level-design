from concurrent.futures import ThreadPoolExecutor

from designs.url_shortener.tiny_url import TinyUrlService

if __name__ == "__main__":
    tiny_url = TinyUrlService(limit=5)
    long_url = "https://longurl.com/longurl/longurl-longurl-longurl/longurl"

    with ThreadPoolExecutor() as executor:
        for i in range(1_000):
            executor.submit(tiny_url.shorten_url, long_url=f"{long_url}/{i}")

    print("-" * 20)
    print("\n".join(tiny_url.reverse_map))
