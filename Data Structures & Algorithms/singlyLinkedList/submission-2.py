
class Node:
    def __init__(self,val:int=0):
        self.next = None
        self.val = val

class LinkedList: 
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        i=0
        if curr and index == 0:
            return curr.val
        while curr and i < index:
            i+=1
            curr = curr.next
        if not curr:
            return -1
        return curr.val

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode

    def insertTail(self, val: int) -> None:
        curr = self.head
        if not curr:
            self.insertHead(val)
        else:
            while curr and curr.next:
                curr = curr.next
            curr.next = Node(val)

    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0 
        if self.head and index == 0:
            self.head = self.head.next
            return True
        else:
            while cur and i < index-1: 
                cur = cur.next
                i+=1
            if not cur or not cur.next:
                return False
            else:
                cur.next = cur.next.next
        return True

    def getValues(self) -> List[int]:
        cur = self.head
        res = []
        while cur:
            res.append(cur.val)
            cur=cur.next
        return res