import collections


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph =  defaultdict(list)
        for (src,dst) in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        visited = [False]*n

        def bfs(source):
            visited[source] = True
            queue = collections.deque([source])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
        def dfs(source):
            visited[source] = True
            for neighbor in graph[source]:
                if not visited[neighbor]:
                    dfs(neighbor)
        components = 0
        for v in range(n):
            if not visited[v]:
                components += 1
                dfs(v)
        return components



