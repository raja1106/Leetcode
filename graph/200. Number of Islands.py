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


