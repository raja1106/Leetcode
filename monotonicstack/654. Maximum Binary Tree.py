class Solution_Bruteforce:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(lo, hi):
            if lo > hi:
                return None
            max_idx = lo
            for i in range(lo + 1, hi + 1):
                if nums[i] > nums[max_idx]:
                    max_idx = i
            root = TreeNode(nums[max_idx])
            root.left  = build(lo, max_idx - 1)
            root.right = build(max_idx + 1, hi)
            return root
        return build(0, len(nums) - 1)


from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution_Best_One_Pass:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []

        for num in nums:
            current = TreeNode(num)

            # All smaller elements on the left side of current
            # should become part of current's left subtree.
            while stack and stack[-1].val < num:
                current.left = stack.pop()

            # If stack is not empty, current is smaller than stack[-1].
            # So current becomes the right child of stack[-1].
            if stack:
                stack[-1].right = current

            stack.append(current)

        # Bottom of the stack is the root.
        return stack[0] if stack else None


from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution_Naive:#O(n)
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # Monotonic decreasing stack.
        #
        # The stack stores nodes in decreasing order of value.
        # Example:
        # nums = [3, 2, 1]
        # stack = [3, 2, 1]
        #
        # When we see a bigger number later, all smaller nodes before it
        # should become part of its left subtree.
        st = []

        for num in nums:
            # Create a tree node for the current number.
            new_node = TreeNode(num)

            # Case 1:
            # If the stack is empty, this is the first node.
            #
            # Case 2:
            # If the current number is smaller than the stack top,
            # it means current number should appear somewhere on the right side
            # of the previous bigger number.
            #
            # We do not connect it immediately here.
            # We just keep it in the stack and connect right children at the end.
            if not st or st[-1].val > num:
                st.append(new_node)
                continue

            # This list will temporarily store all nodes smaller than current number.
            #
            # Example:
            # nums = [3, 2, 1, 6]
            #
            # When num = 6:
            # stack has [3, 2, 1]
            # We pop 1, 2, 3 because all are smaller than 6.
            #
            # temp_list becomes [1, 2, 3]
            temp_list = []

            # Pop all nodes that are smaller than current number.
            #
            # These popped nodes belong to the left subtree of current node
            # because they appeared before current number and are smaller than it.
            while st and num > st[-1].val:
                temp_list.append(st.pop())

            # Now rebuild the popped nodes as a right-skewed tree.
            #
            # Example:
            # temp_list = [1, 2, 3]
            #
            # We need to build:
            #
            #     3
            #      \
            #       2
            #        \
            #         1
            #
            # This becomes the left subtree of the current bigger node.
            left_root_node = None
            current = None

            while temp_list:
                # Pop from temp_list to get nodes in reverse order.
                # For [1, 2, 3], this gives 3 first, then 2, then 1.
                node = temp_list.pop()

                # First popped node becomes the root of the left subtree.
                if not left_root_node:
                    left_root_node = node
                    current = node
                else:
                    # Attach the next smaller node as the right child.
                    current.right = node
                    current = node

            # Attach the rebuilt subtree as the left child of current node.
            #
            # Example:
            #
            #        6
            #       /
            #      3
            #       \
            #        2
            #         \
            #          1
            new_node.left = left_root_node

            # Push the current node into the stack.
            #
            # There may still be a bigger node before it in the stack.
            # That connection will be handled in the final right-chain step.
            st.append(new_node)

        # After processing all numbers, the stack contains remaining nodes
        # in decreasing order.
        #
        # These nodes should be connected as right children.
        #
        # Example:
        # stack = [7, 6, 5]
        #
        # Build:
        #
        #     7
        #      \
        #       6
        #        \
        #         5
        root_node = None
        current = None

        for node in st:
            # First node in the stack is the root of the final tree.
            if not root_node:
                root_node = node
                current = node
            else:
                # Remaining nodes become right children.
                current.right = node
                current = node

        return root_node