# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        n=0
        digit1=digit2=0
        while cur1:
            digit1+=cur1.val * pow(10, n)
            cur1=cur1.next
            n+=1
        n=0
        while cur2:
            digit2+=cur2.val*pow(10,n)
            cur2=cur2.next
            n+=1
        print(f"digit1: ", digit1,  f"\ndigit2: ", digit2)
        total = digit1+digit2
        if total == 0: return ListNode(0)
        
        dummy = ListNode()
        curNew = dummy
        while total > 0:
            num = total % 10
            curNew.next = ListNode(num)
            curNew = curNew.next
            total //= 10
        return dummy.next