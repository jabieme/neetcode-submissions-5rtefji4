# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1=[]
        res2=[]

        def dfs(root,res):
            if not root:
                res.append(None)
                return
            dfs(root.left,res)
            dfs(root.right,res)
            res.append(root.val)
            return res
        print(dfs(p,res1))
        print(dfs(q,res2))
        return dfs(p,res1) == dfs(q,res2)