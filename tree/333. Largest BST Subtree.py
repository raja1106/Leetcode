# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        max_size = 1
        if root is None:
            return 0
        def dfs(node):
            my_smallest = my_largest = node.val
            if node.left is None and node.right is None:
                return (True, my_smallest, my_largest, 1)
            amibst = True
            my_size = 1
            if node.left:
                (is_leftbst, smallest, largest, left_size) = dfs(node.left)
                if not is_leftbst or largest >= node.val:
                    amibst = False
                else:
                    my_smallest = smallest
                    my_size += left_size
            if node.right:
                (is_rightbst, smallest, largest, right_size) = dfs(node.right)
                if not is_rightbst or smallest <= node.val:
                    amibst = False
                else:
                    my_largest = largest
                    my_size += right_size
            nonlocal max_size
            if amibst and my_size > max_size:
                max_size = max(max_size, my_size)
            return (amibst, my_smallest, my_largest, my_size)

        dfs(root)
        return max_size
