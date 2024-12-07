class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Initialize graph to store the adjacency list of the tree.
        graph = collections.defaultdict(list)

        # Recursively build an undirected graph from the binary tree.
        def build_graph(node):
            if node.left is None and node.right is None:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                build_graph(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                build_graph(node.right)

        # Build the graph from the binary tree
        build_graph(root)

        # List to store the result
        result = []

        # Initialize a set to track visited nodes
        visited = set([target.val])

        # BFS queue initialized with the target node and distance 0
        queue = collections.deque([(target.val, 0)])

        while queue:
            node, distance = queue.popleft()

            # If the current node is at the required distance, add to result
            if distance == k:
                result.append(node)
                continue

            # Explore all neighbors (connected nodes in the graph)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)  # Mark as visited
                    queue.append((neighbor, distance + 1))  # Enqueue with incremented distance

        return result