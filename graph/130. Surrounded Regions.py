class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))

            while queue:
                current_row, current_col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = current_row + dr, current_col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return

        for col in range(cols):
            if board[0][col] == 'O' and (0, col) not in visited:
                bfs(0, col)
                # visited.add((0,col))
            if board[rows - 1][col] == 'O' and (rows - 1, col) not in visited:
                bfs(rows - 1, col)
                # visited.add((rows-1,col))

        for row in range(rows):
            if board[row][0] == 'O' and (row, 0) not in visited:
                bfs(row, 0)
                # visited.add((row,0))
            if board[row][cols - 1] == 'O' and (row, cols - 1) not in visited:
                bfs(row, cols - 1)
                # visited.add((row,cols-1))

        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if board[row][col] == 'O' and (row, col) not in visited:
                    board[row][col] = 'X'

        # return board


