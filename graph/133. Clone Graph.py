# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Dictionary to keep track of copied nodes
        cloned_nodes = {}

        def dfs(node: 'Node') -> 'Node':
            if node in cloned_nodes:
                return cloned_nodes[node]

            # Clone the node
            clone = Node(node.val)
            cloned_nodes[node] = clone

            # Clone all the neighbors recursively
            if node.neighbors:
                clone.neighbors = [dfs(neighbor) for neighbor in node.neighbors]

            return clone

        # Start DFS from the input node
        return dfs(node)


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque


class Solution_Using_BFS:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # Dictionary to keep track of cloned nodes
        cloned_nodes = {node: Node(node.val)}

        # Use a queue for BFS
        queue = deque([node])

        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in cloned_nodes:
                    # Clone the neighbor and add it to the dictionary
                    cloned_nodes[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # Append the cloned neighbor to the current node's clone's neighbors list
                cloned_nodes[current].neighbors.append(cloned_nodes[neighbor])

        return cloned_nodes[node]
