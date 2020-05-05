from src.tool.struct import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def is_valid_bst(node: TreeNode, left=None, right=None):
            if node is None:
                return True
            if left is not None and node.val <= left:
                return False
            if right is not None and node.val >= right:
                return False
            return is_valid_bst(node.left, left, node.val) and is_valid_bst(node.right, node.val, right)

        return is_valid_bst(root)



