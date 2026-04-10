# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, root: Optional[TreeNode], path_min: int, path_max: int) -> bool:
        if not root:
            return True
        
        if root.val <= path_min:
            return False
        elif root.val >= path_max:
            return False
        
        return self.dfs(root.left, path_min, root.val) and self.dfs(root.right, root.val, path_max)
