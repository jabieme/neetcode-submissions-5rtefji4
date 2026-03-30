# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getTail(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head.next
        prev = head
        while cur.next:
            cur = cur.next
            prev = prev.next
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        if not cur.next:
            return
        while cur and cur.next:
            prev = self.getTail(head)
            tail = prev.next
            hold = cur.next
            prev.next = None
            tail.next = cur.next
            cur.next = tail
            cur = hold
           