class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.count -= 1
        if self.count >= self.capacity:
            self.cache.pop(list(self.cache)[0])
            self.count -= 1
        self.cache[key] = value
        self.count += 1