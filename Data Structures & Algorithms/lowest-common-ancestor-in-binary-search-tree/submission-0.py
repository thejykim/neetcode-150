# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = TreeNode(float('inf'))
        self.dfs(root, min(p.val, q.val), max(p.val, q.val))

        return self.res

    def dfs(self, root: TreeNode, p: int, q: int) -> bool:
        if not root:
            return False
        
        if root.val < p:
            return self.dfs(root.right, p, q)
        elif root.val > q:
            return self.dfs(root.left, p, q)
        else:
            self.res = root
            return True