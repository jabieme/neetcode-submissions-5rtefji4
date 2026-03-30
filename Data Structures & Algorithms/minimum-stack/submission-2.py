class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(val, self.minimum)

    def pop(self) -> None:
        if self.stack[len(self.stack)-1] == self.minimum:
            self.stack.pop()
            if self.stack:
                self.minimum = min(self.stack)
            else:
                self.minimum = float('inf')
        else:
            self.stack.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.minimum
