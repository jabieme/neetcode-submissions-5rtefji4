class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0]*capacity
        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i]=n

    def pushback(self, n: int) -> None:
        print(self.arr)
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size]=n
        self.size+=1

    def popback(self) -> int:
        num = self.arr.pop(self.size-1)
        self.size-=1
        return num

    def resize(self) -> None:
        tmp = self.arr
        self.capacity*=2
        newArr = [0]*self.capacity
        self.arr = newArr
        for i in range(self.size):
            self.arr[i] = tmp[i]

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity