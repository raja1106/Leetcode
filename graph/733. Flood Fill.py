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
