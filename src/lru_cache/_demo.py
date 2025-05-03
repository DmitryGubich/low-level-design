from cache import LRUCache

if __name__ == "__main__":
    cache = LRUCache(capacity=3)

    cache.put(key=1, value="Value 1")
    cache.put(key=2, value="Value 2")
    cache.put(key=3, value="Value 3")

    assert cache.get(key=1) == "Value 1"
    assert cache.get(key=2) == "Value 2"

    cache.put(key=4, value="Value 4")

    assert cache.get(key=3) is None
    assert cache.get(key=4) == "Value 4"
