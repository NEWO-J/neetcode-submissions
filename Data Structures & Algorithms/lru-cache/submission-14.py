class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.limit = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key, last=False)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key, last=False)
        if len(self.cache) > self.limit:
            self.cache.popitem()

        return None
