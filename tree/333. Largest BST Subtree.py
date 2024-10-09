# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree_usual_template(self, root: Optional[TreeNode]) -> int:
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
                (is_leftbst, left_smallest, left_largest, left_size) = dfs(node.left)
                if not is_leftbst or left_largest >= node.val:
                    amibst = False
                else:
                    my_smallest = left_smallest
                    my_size += left_size
            if node.right:
                (is_rightbst, right_smallest, right_largest, right_size) = dfs(node.right)
                if not is_rightbst or right_smallest <= node.val:
                    amibst = False
                else:
                    my_largest = right_largest
                    my_size += right_size
            nonlocal max_size
            if amibst and my_size > max_size:
                max_size = max(max_size, my_size)
            return (amibst, my_smallest, my_largest, my_size)

        dfs(root)
        return max_size

    def largestBSTSubtree_optimized(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                # Base case: Empty subtree
                return (True, float('inf'), float('-inf'), 0)

            left_is_bst, left_min, left_max, left_size = dfs(node.left)
            right_is_bst, right_min, right_max, right_size = dfs(node.right)

            # Check if the current node is a valid BST root
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                current_min = min(left_min, node.val)
                current_max = max(right_max, node.val)
                current_size = left_size + right_size + 1
                self.max_size = max(self.max_size, current_size)
                return (True, current_min, current_max, current_size)
            else:
                return (False, float('-inf'), float('inf'), 0)

        self.max_size = 0
        dfs(root)
        return self.max_size
