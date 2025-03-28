# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildBST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            return root

        return buildBST(0, len(nums) - 1)


class Solution_Iterative:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        # Calculate the root using the middle element of the entire array
        start, end = 0, len(nums) - 1
        mid = start + (end - start) // 2
        root = TreeNode(nums[mid])

        # Each tuple: (parent, start, end, is_left_child)
        # For the root, we don't need a parent, so we create tasks for its children.
        stack = []
        # Create tasks for left and right subtree of the root.
        stack.append((root, start, mid - 1, True))  # Left subtree task
        stack.append((root, mid + 1, end, False))  # Right subtree task

        # Process the stack until all tasks are completed.
        while stack:
            parent, left, right, is_left = stack.pop()

            # If the subarray is empty, there's no node to create.
            if left > right:
                continue

            # Choose the middle element as the root for this subtree.
            mid = left + (right - left) // 2
            node = TreeNode(nums[mid])

            # Attach the node to the parent.
            if is_left:
                parent.left = node
            else:
                parent.right = node

            # Push tasks for the left and right children of the current node.
            stack.append((node, left, mid - 1, True))  # Left subtree of this node
            stack.append((node, mid + 1, right, False))  # Right subtree of this node

        return root
