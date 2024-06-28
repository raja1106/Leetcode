from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(n)]
        for (src, dst) in edges:
            adjlist[src].append(dst)
            adjlist[dst].append(src)
        visited = [-1] * n

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
                if components > 1:
                    return False
                dfs(v)
        return True

'''
    adjlist = [[] for _ in range(n)]
        for (src,dst) in edges:
            adjlist[src].append(dst)
            adjlist[dst].append(src)

        visited = [-1]*n
        parent = [-1]*n
        def dfs(source):
            visited[source] = 1
            for neighbor in adjlist[source]:
                if visited[neighbor] == -1:
                    parent[neighbor] = source
                    if dfs(neighbor):
                        return True
                else:
                    if parent[source] != neighbor:
                        return True
            return False

        for v in range(n):
            if visited[v] == -1:
                dfs(v)
        return True
'''


class Solution1:
    isCycle = False

    def bfs(self, src: int, adjList: List[List[int]], visited: set, parent: List[int]):

        visited.add(src)
        # parent[src] = -1
        queue = deque()
        queue.append(src)

        while len(queue) > 0:
            src = queue.popleft()
            neighbourList = adjList[src]
            for neighbour in neighbourList:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    parent[neighbour] = src
                else:
                    if parent[src] != neighbour:
                        self.isCycle = True
                        return

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = []
        parent = []

        # declare the adjacency list
        for _ in range(n):
            parent.append(-1)
            adjList.append([])

        # iterate and insert the edges inside the adj list
        for edge in edges:
            src = edge[0]
            dest = edge[1]
            adjList[src].append(dest)
            adjList[dest].append(src)

        visited = set()
        self.bfs(0, adjList, visited, parent)

        if len(visited) != n or self.isCycle == True:
            return False

        return True

