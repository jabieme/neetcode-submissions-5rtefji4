# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def printQueue(self, q: List[int]) -> List[int]:
        copy = []
        for i in range(len(q)):
            copy.append(q[i].val)
        return copy
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        res = []

        if root:
            queue.append(root)
            res.append(root.val)
        
        while len(queue) > 0:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if len(queue) > 1:
                res.append(queue[1].val)
            elif queue:
                res.append(queue[0].val)
                
        return res