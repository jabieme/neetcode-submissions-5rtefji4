# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        result=[]
        def dfs(root):
            nonlocal result
            if not root:
                return True
            dfs(root.left)
            dfs(root.right)
            result.append(self.sameTree(root,subRoot))
            
        res = dfs(root)
       
        for r in result:
            if r:
                return True
        return False
    
    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        
        if root1 and root2 and root1.val == root2.val:
            return self.sameTree(root1.left,root2.left) and self.sameTree(root1.right, root2.right)
        else:
            return False