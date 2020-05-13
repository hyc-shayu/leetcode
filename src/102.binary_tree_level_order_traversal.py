# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
from src.tool.struct import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q1, q2 = [root], []
        res = []
        while q1:
            res.append([])
            for node in q1:
                res[-1].append(node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            q1, q2 = q2, []

        return res
