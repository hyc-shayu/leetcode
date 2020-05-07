# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from src.tool.struct import TreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs_check(s_node, t_node=t):
            if not s_node and not t_node:
                return True
            elif s_node and t_node and s_node.val == t_node.val:
                return dfs_check(s_node.left, t_node.left) and dfs_check(s_node.right, t_node.right)
            else:
                return False

        def dfs(root=s):
            return dfs_check(root) or (dfs(root.left) or dfs(root.right)) if root else False
        return dfs()

    def kmp_is_subtree(self, s: TreeNode, t: TreeNode) -> bool:
        pass
