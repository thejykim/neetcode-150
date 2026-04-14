# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = 0

        self.dfs(root, k)

        return self.res
    
    def dfs(self, node: Optional[TreeNode], k: int):
        if not node or self.count == k:
            return
        
        self.dfs(node.left, k)

        self.count += 1

        if self.count == k:
            self.res = node.val
            return

        self.dfs(node.right, k)