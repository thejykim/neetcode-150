# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = []
        self.dfs(root, float('-inf'))

        return len(self.res)
    
    def dfs(self, root: TreeNode, path_max: int):
        if not root:
            return
        
        if root.val >= path_max:
            self.res.append(root.val)
            path_max = root.val
        
        self.dfs(root.left, path_max)
        self.dfs(root.right, path_max)