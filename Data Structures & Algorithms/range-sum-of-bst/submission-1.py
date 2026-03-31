# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = deque()
        total = 0

        queue.append(root)

        while queue:
            popped = queue.popleft()
            if popped:
                queue.append(popped.left)
                queue.append(popped.right)

                if popped.val >= low and popped.val <= high:
                    total += popped.val
    
        return total