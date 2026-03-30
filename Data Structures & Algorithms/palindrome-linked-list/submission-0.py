# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow

        while cur:
            tmp1 = cur.next
            cur.next = prev
            prev = cur
            cur = tmp1
        
        newHead = head

        while prev:
            if prev.val != newHead.val:
                return False
            prev=prev.next
            newHead=newHead.next
    
        return True