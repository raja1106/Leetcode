class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        destination_node = len(graph) - 1
        result = []

        def dfs(node, path):
            # Append the current node to the path
            path.append(node)

            # If the destination is reached, add the path to the result
            if node == destination_node:
                result.append(path[:])  # Make a copy of the path
            else:
                # Explore the neighbors of the current node
                for neighbor in graph[node]:
                    dfs(neighbor, path)

            # Backtrack by removing the current node
            path.pop()

        # Start DFS from node 0
        dfs(0, [])
        return result
