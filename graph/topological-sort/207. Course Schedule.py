from collections import defaultdict, deque
from typing import List

class Solution_Using_BFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        return len(topological_order) == numCourses

class Solution_Using_DFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True

        graph = defaultdict(list)
        for dst, src in prerequisites:
            graph[src].append(dst)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        state = [UNVISITED] * numCourses

        def has_cycle(node: int) -> bool:
            if state[node] == VISITING:
                return True
            if state[node] == VISITED:
                return False

            state[node] = VISITING
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            state[node] = VISITED
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True
