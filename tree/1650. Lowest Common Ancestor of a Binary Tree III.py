# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q

        # Traverse upwards to find the LCA
        while p1 != p2:
            # If p1 reaches the root, start from q
            p1 = p1.parent if p1 else q
            # If p2 reaches the root, start from p
            p2 = p2.parent if p2 else p

        return p1


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


class Node: # Without Parent node solving the problem
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowestCommonAncestor(nodes, p_start, q_start):
    """
    nodes   : A list of all nodes in the tree (similar to std::vector<Node*> in C++).
    p_start : The starting node p (Node* p_start in C++).
    q_start : The starting node q (Node* q_start in C++).
    Returns the lowest common ancestor of p and q.
    """
    # Create a mapping from child -> parent
    child_to_parent = {}

    # Fill the child_to_parent map
    for node in nodes:
        if node.left:
            child_to_parent[node.left] = node
        if node.right:
            child_to_parent[node.right] = node

    p = p_start
    q = q_start

    # Traverse upwards until p and q meet
    while p != q:
        # If p has a parent, move p to its parent; otherwise, reset p to p_start
        if p in child_to_parent:
            p = child_to_parent[p]
        else:
            p = p_start

        # If q has a parent, move q to its parent; otherwise, reset q to p_start
        if q in child_to_parent:
            q = child_to_parent[q]
        else:
            q = p_start

    return p  # p (or q) is now the LCA
