# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a, b = p, q

        # Traverse upwards to find the LCA
        while a != b:
            # If a reaches the root, start from q
            a = a.parent if a else q
            # If b reaches the root, start from p
            b = b.parent if b else p

        return a


# Example usage
# Constructing a simple binary tree with parent pointers:
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4
root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.parent = root
root.right.parent = root
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.left.parent = root.left
root.left.right.parent = root.left
root.right.left.parent = root.right
root.right.right.parent = root.right
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.left.right.left.parent = root.left.right
root.left.right.right.parent = root.left.right

solution = Solution()
p = root.left  # Node with value 5
q = root.left.right.right  # Node with value 4

ancestor = solution.lowestCommonAncestor(p, q)
print(f"The lowest common ancestor of nodes {p.val} and {q.val} is node {ancestor.val}")
# Output: The lowest common ancestor of nodes 5 and 4 is node 5