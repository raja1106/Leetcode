import collections


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = [[] for _ in range(n)]
        for (src,dst) in edges:
            adjlist[src].append(dst)
            adjlist[dst].append(src)
        visited = [-1]*n

        def bfs(source):
            visited[source] = 1
            queue = collections.deque([source])
            while queue:
                node = queue.popleft()
                for neighbor in adjlist[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1
                        queue.append(neighbor)


        def dfs(source):
            visited[source] = 1
            for neighbor in adjlist[source]:
                if visited[neighbor] == -1:
                    dfs(neighbor)
        components = 0
        for v in range(n):
            if visited[v] == -1:
                components += 1
                dfs(v)
        return components



