class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        kth_value = None

        def in_order(node):
            nonlocal count, kth_value
            # Early return if kth element has been found
            if kth_value is not None:
                return
            if node.left:
                in_order(node.left)

            count += 1
            if count == k:
                kth_value = node.val
                return  # Once found, we can return immediately
            if node.right:
                in_order(node.right)

        if not root:
            return -1

        in_order(root)
        return kth_value


class OSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1  # number of nodes in subtree including self


def update_size(node):
    if node:
        node.size = 1
        if node.left:
            node.size += node.left.size
        if node.right:
            node.size += node.right.size


def insert(root, val):
    """Insert a new value into the BST and update subtree sizes.
       Note: This does not include balancing, so worst-case time is O(n)."""
    if root is None:
        return OSTNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    update_size(root)
    return root  # In a full implementation, you'd balance the tree here.


def kth_smallest(root, k):
    """Return the kth smallest element in the tree."""
    if not root:
        return None  # or raise an exception

    # Number of nodes in left subtree.
    left_size = root.left.size if root.left else 0

    if k == left_size + 1:
        return root.val
    elif k <= left_size:
        return kth_smallest(root.left, k)
    else:
        # Search in right subtree with updated k.
        return kth_smallest(root.right, k - left_size - 1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution_kthLargest:
    def kthLargest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Finds the kth largest element in a BST.
        """
        count = 0
        kth_value = -1

        def reverse_in_order(node):
            nonlocal count, kth_value
            # Early return if node is None or kth largest has been found
            if not node or kth_value != -1:
                return
            # Traverse the right subtree first
            reverse_in_order(node.right)

            count += 1
            if count == k:
                kth_value = node.val
                return

            # Traverse the left subtree after processing current node
            reverse_in_order(node.left)

        if not root:
            return -1

        reverse_in_order(root)
        return kth_value


# Example usage:
values = [5, 3, 6, 2, 4, 1]
root = None
for v in values:
    root = insert(root, v)

print("3rd smallest element is:", kth_smallest(root, 3))
