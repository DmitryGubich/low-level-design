BASE = 62
CHARSET_DEFAULT = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def encode(n: int) -> str:
    chs = []
    while n > 0:
        n, r = divmod(n, BASE)
        chs.insert(0, CHARSET_DEFAULT[r])

    if not chs:
        return "0"

    return "".join(chs)
