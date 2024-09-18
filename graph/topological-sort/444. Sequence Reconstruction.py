class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        # Initialize graph and in-degrees
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        # Build the graph
        for sequence in sequences:
            for i in range(len(sequence) - 1):
                u, v = sequence[i], sequence[i + 1]
                graph[u].append(v)
                in_degree[v] += 1

        # Topological sort using BFS (Kahn's Algorithm)
        queue = deque([node for node in nums if in_degree[node] == 0])
        topological_order = []
        while queue:
            # If there is more than one node in the queue, the sequence is not unique
            if len(queue) > 1:
                return False
            node = queue.popleft()
            topological_order.append(node)
            # Ensure the node element matches the nums order

            # Process neighbors
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check if the topological sort includes all elements in nums
        return len(topological_order) == len(nums)