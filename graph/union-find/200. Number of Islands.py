class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            grid[r][c] = '2'
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    # grid[nr][nc] = '2'
                    dfs(nr, nc)

        def bfs(r, c):
            queue = deque()
            grid[r][c] = 2
            queue.append((r, c))
            while queue:
                current_row, current_col = queue.popleft()
                for dr, dc in directions:
                    nr = current_row + dr
                    nc = current_col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '2'
                        queue.append((nr, nc))

        number_islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    number_islands += 1
                    #bfs(row, col) # you can use either approach here
                    dfs(row,col)

        return number_islands


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size
        self.components = size

    def find(self, x):
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


class Solution_Union_Find_Approach:
    def numIslands(self, grid):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(rows * cols)
        directions = [(0, 1), (1, 0)]  # Right, Down
        water_count = 0
        # Step 1: Union adjacent land cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            uf.union(r * cols + c, nr * cols + nc)
                else:
                    water_count += 1

        # Step 2: Count distinct roots for land cells
        unique_islands = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    set_name = uf.find(r * cols + c)
                    unique_islands.add(set_name)

        return len(unique_islands)


# Example Usage
solution = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(solution.numIslands(grid))  # Output: 1
