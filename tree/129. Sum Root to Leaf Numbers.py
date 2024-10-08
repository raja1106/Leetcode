# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''

    '''
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        def getvalue(slate):
            str_val = ''.join(slate)
            return int(str_val)

        def dfs(node, slate):
            nonlocal total
            if node.left is None and node.right is None:
                slate.append(str(node.val))
                total += getvalue(slate)
                slate.pop()
                return

            if node.left:
                slate.append(str(node.val))
                dfs(node.left, slate)
                slate.pop()
            if node.right:
                slate.append(str(node.val))
                dfs(node.right, slate)
                slate.pop()

        if not root:
            return 0
        dfs(root, [])
        return total


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1: # this one is more efficient
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_number):
            if not node:
                return 0

            current_number = current_number * 10 + node.val

            # If it's a leaf node, return the current number
            if not node.left and not node.right:
                return current_number

            # Recursively sum the numbers from the left and right subtrees
            left_sum = dfs(node.left, current_number)
            right_sum = dfs(node.right, current_number)

            return left_sum + right_sum

        # Initiate the DFS traversal with the root and an initial number 0
        return dfs(root, 0)

# Example usage:
# root = TreeNode(1, TreeNode(2), TreeNode(3))
# solution = Solution()
# print(solution.sumNumbers(root))  # Output: 25 (12 + 13)
