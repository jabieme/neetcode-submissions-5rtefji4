class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        deep_copy = Node(head.val)
        cur = head.next
        cur_copy = deep_copy
        
        while cur:
            cur_copy.next = Node(x=cur.val)
            cur = cur.next
            cur_copy = cur_copy.next
        self.findRandom(head, deep_copy)
        return deep_copy
    
    def findRandom(self, head, copy):
        cur = head
        cur_copy = copy
        while cur_copy:
            if cur.random == None:
                cur_copy.random = None
            else:
                iterator = copy
                orig_iterator = head
                while orig_iterator != cur.random:
                    iterator = iterator.next
                    orig_iterator = orig_iterator.next
                cur_copy.random = iterator
            cur_copy = cur_copy.next
            cur = cur.next