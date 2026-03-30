class MaxStack:

    def __init__(self):
        self.stack = []
        self.maxNum = []

    def push(self, x: int) -> None:
        self.stack.append(x)
    
        if not self.maxNum or self.maxNum[-1] <= x:
            self.maxNum.append(x)

    def pop(self) -> int:
        res = self.stack.pop()
        if res == self.maxNum[-1]:
            self.maxNum.pop()
        return res

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        print(self.maxNum)
        return self.maxNum[-1]

    def popMax(self) -> int:
        test = []
        while self.stack[-1]!=self.maxNum[-1]:
            test.append(self.stack.pop())
        print("test:",test)
        print("stack:",self.stack)
        print("maxStack:",self.maxNum)
        popped = self.stack.pop()
        self.maxNum.pop()
        while len(test)>0:
            self.push(test.pop())
        print("stack:",self.stack)
        print("max:",self.maxNum)
        return popped
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
