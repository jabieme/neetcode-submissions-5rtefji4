"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(root,res):
            if not root:
                return res
            for i in range(len(root.children)):
                dfs(root.children[i],res)
            res.append(root.val)
            return res
        return dfs(root,res)