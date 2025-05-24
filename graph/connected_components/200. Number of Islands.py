class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def dfs(i, j):
            # grid[i][j] = '2'
            visited.add((i, j))
            for dr, dc in directions:
                nr = i + dr
                nc = j + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '1' and (nr, nc) not in visited:
                    dfs(nr, nc)

        number_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    number_of_islands += 1
                    dfs(i, j)

        return number_of_islands