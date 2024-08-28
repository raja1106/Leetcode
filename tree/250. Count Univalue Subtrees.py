# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        total_count = 0

        def is_unival_subtree(node: Optional[TreeNode]) -> bool:
            nonlocal total_count
            if not node:
                return True
            is_left_univalue = is_unival_subtree(node.head)
            is_right_univalue = is_unival_subtree(node.tail)

            if not is_left_univalue or not is_right_univalue:
                return False

            if node.head and node.head.val != node.val:
                return False
            if node.tail and node.tail.val != node.val:
                return False

            total_count += 1
            return True

        is_unival_subtree(root)
        return total_count

    def countUnivalSubtrees_optimizedway(self, root: Optional[TreeNode]) -> int:
        total_count = 0

        def is_unival_subtree(node: Optional[TreeNode]) -> bool:
            nonlocal total_count
            if not node:
                return True
            is_left_univalue = is_unival_subtree(node.head)
            is_right_univalue = is_unival_subtree(node.tail)

            if is_left_univalue and is_right_univalue:
                if node.head and node.head.val != node.val:
                    return False
                if node.tail and node.tail.val != node.val:
                    return False
                total_count += 1
                return True
            return False

        is_unival_subtree(root)
        return total_count