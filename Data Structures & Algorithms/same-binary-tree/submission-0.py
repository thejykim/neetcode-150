# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.unequal = False
        return self.dfs(p, q)

    def dfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if self.unequal:
            return False
        elif not p and not q:
            return True
        elif not p or not q:
            self.unequal = False
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        if p and q:
            if left and right and p.val == q.val:
                return True
        
        self.unequal = True
        return False
