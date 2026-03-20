from typing import List

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.size = [1] * size
        self.components = 0  # will represent current #islands among "active" cells

    def find(self, x: int) -> int:
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by size
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            self.components -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # Step 1: Setup DSU over all cells, but only "activate" when land is added
        uf = UnionFind(m * n)
        is_land = [False] * (m * n)

        def idx(r: int, c: int) -> int:
            return r * n + c

        res = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 2: Add lands one by one and union with adjacent lands
        for r, c in positions:
            cur = idx(r, c)

            # If duplicate position, island count doesn't change
            if is_land[cur]:
                res.append(uf.components)
                continue

            is_land[cur] = True
            uf.components += 1  # new land starts as a new island

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nei = idx(nr, nc)
                    if is_land[nei]:
                        uf.union(cur, nei)

            res.append(uf.components)

        return res
