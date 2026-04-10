# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = dict()
        self.dfs(root, 0)

        return list(self.res.values())

    def dfs(self, root: Optional[TreeNode], depth: int):
        if not root:
            return

        depth_list = self.res.get(depth, list())
        depth_list.append(root.val)
        self.res[depth] = depth_list
        
        left = self.dfs(root.left, depth + 1)
        right = self.dfs(root.right, depth + 1)

        return