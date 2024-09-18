class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Edge case: No numCourses, return True
        if numCourses == 0:
            return True

        # Build the graph and calculate in-degrees for each course
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for dst, src in prerequisites:
            graph[src].append(dst)
            in_degree[dst] += 1  # Increase in-degree of destination course

        # Initialize a queue with all nodes having in-degree of 0
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        topological_order = []

        # Process nodes with BFS
        while queue:
            node = queue.popleft()
            topological_order.append(node)

            # For all neighbors, reduce their in-degree by 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                # If in-degree becomes 0, add the neighbor to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If we processed all the nodes, return True; otherwise, there was a cycle
        return topological_order if len(topological_order) == numCourses else []
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Edge case: No numCourses, return True
        if numCourses == 0:
            return True
        visited = [False] * numCourses
        topological_order = []
        graph = defaultdict(list)
        for dst, src in prerequisites:
            graph[src].append(dst)
        on_stack = set()
        def has_cycle(node: int) -> bool:
            visited[node] = True
            on_stack.add(node)
            for neighbour in graph[node]:
                if neighbour in on_stack:  # Cycle detected (back edge)
                    return True
                if not visited[neighbour]:
                    if has_cycle(neighbour):  # If a cycle is detected, return True
                        return True
            # Add node to the topological order and remove it from the recursion stack
            topological_order.append(node)
            on_stack.remove(node)
            return False

        # Perform DFS on all nodes
        for u in range(numCourses):
            if not visited[u]:
                if has_cycle(u):  # If a cycle is detected, return False
                    return []  # return [] if topological_order is requested
        # If no cycle is detected, return True indicating valid scheduling is possible
        return topological_order[::-1]  # topological_order[::-1]