# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from src.tool.struct import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = TreeNode(-1)

        def dfs(node):
            if not node:
                return False
            l_res = dfs(node.left)
            r_res = dfs(node.right)
            nonlocal ans
            if ans:
                return False
            if l_res and r_res or ((node is p or node is q) and (l_res or r_res)):
                ans = node
                return True
            return l_res or r_res or (node is p or node is q)
        dfs(root)
        return ans
