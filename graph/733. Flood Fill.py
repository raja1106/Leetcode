from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startColor = image[sr][sc]
        new_color = color
        if startColor == new_color:
            return image
        rows, cols = len(image), len(image[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row: int, col: int) -> None:
            if image[row][col] == startColor:
                image[row][col] = new_color
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        dfs(nr, nc)
        dfs(sr, sc)
        return image
class Solution_Using_BFS:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        old_color = image[sr][sc]
        if old_color == color:
            return image
        queue = deque()
        image[sr][sc] = color
        queue.append((sr,sc))

        while queue:
            current_row,current_col = queue.popleft()
            #image[current_row][current_col] = color

            for dr,dc in directions:
                nr,nc = current_row+dr,current_col+dc
                if 0<=nr<len(image) and 0<=nc<len(image[0]) and image[nr][nc] == old_color:
                    image[nr][nc] = color
                    queue.append((nr,nc))

        return image