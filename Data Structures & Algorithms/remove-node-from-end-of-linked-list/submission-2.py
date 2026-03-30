# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]):
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        head = self.reverse(head)
        cur = head
        if n == 1:
            return self.reverse(cur.next)
        
        for _ in range(n-2):
            cur = cur.next
        cur.next = cur.next.next
        return self.reverse(head)
        
