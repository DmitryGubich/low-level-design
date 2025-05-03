class Node:
    def __init__(self, key: int | None, value: str | None) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"{self.key}: {self.value}"


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}
        self.head = Node(key=None, value=None)
        self.tail = Node(key=None, value=None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node=node)
            return node.value
        return None

    def put(self, key: int, value: str) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node=node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node=node)
            if len(self.cache) > self.capacity:
                removed_node = self._remove_tail()
                del self.cache[removed_node.key]

    def _add_to_head(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node: Node) -> None:
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_tail(self) -> Node:
        node = self.tail.prev
        self._remove_node(node=node)
        return node
