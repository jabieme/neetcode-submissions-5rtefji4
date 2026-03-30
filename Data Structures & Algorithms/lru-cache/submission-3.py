class LRUCache:

    def __init__(self, capacity: int):
        self.queue = deque()
        self.capacity = capacity
        self.hashmap = {}

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.queue.remove(key)
            self.queue.append(key)
            return self.hashmap[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.queue.remove(key)
        elif len(self.queue) >= self.capacity:
            popped = self.queue.popleft()
            self.hashmap.pop(popped)
        
        self.hashmap[key] = value
        self.queue.append(key)