# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from src.tool.struct import TreeNode
from src.tool.test_data import string_to_tree_node
from typing import List, Mapping


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

    def isSubtree_kmp(self, s: TreeNode, t: TreeNode) -> bool:

        def pre_order(root, res):
            if root:
                res.append(root.val)
                pre_order(root.left, res)
                pre_order(root.right, res)
            else:
                res.append(None)

        def compute_kmp(pattern) -> List[Mapping]:
            kmp = {k: 0 for k in pattern}
            kmp = [kmp.copy() for _ in pattern]
            kmp[0][pattern[0]] = 1
            ret_state = 0
            for i in range(1, len(pattern)):
                for k in kmp[i]:
                    if k == pattern[i]:
                        kmp[i][k] = i + 1
                    else:
                        kmp[i][k] = kmp[ret_state][k]
                ret_state = kmp[ret_state][pattern[i]]
            return kmp

        txt, pattern = [], []
        pre_order(s, txt)
        pre_order(t, pattern)

        kmp = compute_kmp(pattern)
        state = 0
        for i in range(len(txt)):
            state = kmp[state].get(txt[i], 0)
            if state == len(pattern):
                return True

        return False


if __name__ == '__main__':
    assert False == Solution().isSubtree_kmp(string_to_tree_node('[3, 4, 5, 1, 2, null, null, 0]'),
                                             string_to_tree_node('[4, 1, 2]'))
