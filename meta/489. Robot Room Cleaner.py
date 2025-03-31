class Solution:
    def cleanRoom(self, robot):
        # Directions represent (row_change, col_change) for up, right, down, and left.
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(x, y, d):
            robot.clean()
            visited.add((x, y))

            for i in range(4):
                new_d = (d + i) % 4
                new_x = x + directions[new_d][0]
                new_y = y + directions[new_d][1]

                if (new_x, new_y) not in visited and robot.move():
                    dfs(new_x, new_y, new_d)
                    go_back()
                robot.turnRight()

        # Start DFS from (0, 0) in the direction up (0).
        dfs(0, 0, 0)