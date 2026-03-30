# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []

        if root:
            queue.append(root)
        while len(queue) > 0:
            new = []
            for _ in range(len(queue)):
                popped = queue.popleft()
                new.append(popped.val)
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right) 
            res.append(new)

        return res