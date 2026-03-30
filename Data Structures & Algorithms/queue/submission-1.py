class Deque:
    
    def __init__(self):
        self.deque = []

    def isEmpty(self) -> bool:
        if len(self.deque) == 0:
            return True
        return False

    def append(self, value: int) -> None:
        self.deque.append(value)

    def appendleft(self, value: int) -> None:
        add = [value]
        self.deque = add+self.deque

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque.pop(len(self.deque)-1)

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        num = self.deque[0]
        self.deque = self.deque[1:len(self.deque)]
        return num
