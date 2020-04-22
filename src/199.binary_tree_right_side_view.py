# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from src.tool.struct import TreeNode
from typing import List
from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = [deque([root]), deque()]
        q_idx = 0
        result = []
        while queue[q_idx]:
            next_idx = (q_idx + 1) & 1
            node = queue[q_idx].popleft()
            queue[next_idx].extend([child for child in (node.left, node.right) if child])
            if not queue[q_idx]:
                result.append(node.val)
                q_idx = next_idx

        return result
