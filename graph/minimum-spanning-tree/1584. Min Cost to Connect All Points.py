class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # Initialize parent array
        self.size = [1] * size  # Initialize size array, each component starts with size 1
        self.components = size  # Number of connected components

    def find(self, x):
        # Path compression: Make all nodes on the path point to the root
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Recursively find the root and compress path
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)  # Find root of x
        rootY = self.find(y)  # Find root of y

        if rootX != rootY:
            # Union by size: Attach the smaller tree under the larger tree
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]  # Update the size of rootY
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]  # Update the size of rootX
            # Decrease the number of components after a successful union
            self.components -= 1

    def connected(self, x, y):
        # Check if two elements are in the same component
        return self.find(x) == self.find(y)

    def get_components(self):
        # Return the number of connected components
        return self.components


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        min_heap = []

        def find_cost(u, v):
            x = points[u]
            y = points[v]
            cost = abs(x[0] - y[0]) + abs(x[1] - y[1])
            return cost

        for i in range(n):
            for j in range(i + 1, n):
                cost = find_cost(i, j)
                min_heap.append((cost, i, j))
        heapify(min_heap)
        total_cost = 0
        while min_heap and uf.get_components() > 1:
            current_cost, src, dst = heappop(min_heap)

            if not uf.connected(src, dst):
                total_cost += current_cost
                uf.union(src, dst)

        return total_cost























