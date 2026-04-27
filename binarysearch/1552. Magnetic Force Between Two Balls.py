class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def can_place(min_dist):
            """Greedy: can we place m balls with at least min_dist apart?"""
            count = 1  # Place first ball at position[0]
            last_placed = position[0]

            for i in range(1, len(position)):
                if position[i] - last_placed >= min_dist:
                    count += 1
                    last_placed = position[i]
                if count == m:
                    return True
            return False

        # Binary search on the answer
        start, end = 1, (position[-1] - position[0]) // (m - 1)
        result = 0
        # lllllLRrrrrrr. end
        while start <= end:
            mid = (start + end) // 2
            if can_place(mid):
                start = mid + 1
            else:
                end = mid - 1  # mid not achievable, try smaller

        return end

class Solution_BruteForce:
    def maxDistance(self, position: List[int], m: int) -> int:
        '''
        1. find min for every combination
        2. update global max after step 1
        '''
        position.sort()
        global_max = -1

        def update_global_max(arr):
            nonlocal global_max
            min_val = float('inf')
            for i in range(len(arr) - 1):
                for j in range(i + 1, len(arr)):
                    distance = abs(arr[i] - arr[j])
                    min_val = min(min_val, distance)

            global_max = max(global_max, min_val)
            return min_val

        def dfs(i, placed_arr, remaining_balls):
            if i == len(position):
                if remaining_balls == 0:
                    update_global_max(placed_arr)
                return
            if remaining_balls == 0:
                update_global_max(placed_arr)
                return

            # exclude
            dfs(i + 1, placed_arr, remaining_balls)
            # include
            placed_arr.append(position[i])
            dfs(i + 1, placed_arr, remaining_balls - 1)
            placed_arr.pop()

        dfs(0, [], m)
        return global_max

class Solution_Top_Down_Memo:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        memo = {}

        def dfs(i, remaining, last_pos):
            """
            Returns: max possible min-distance achievable
                     by placing `remaining` balls in position[i:]
                     given last ball was at last_pos
            Returns -1 if impossible
            """
            if remaining == 0:
                return float('inf')  # No more balls to place; no constraint added
            if i == n:
                return -1            # Positions exhausted, balls remain

            state = (i, remaining, last_pos)
            if state in memo:
                return memo[state]

            best = -1

            # Exclude position[i]
            best = max(best, dfs(i + 1, remaining, last_pos))

            # Include position[i]
            dist = position[i] - last_pos
            future_best = dfs(i + 1, remaining - 1, position[i])
            if future_best != -1:
                best = max(best, min(dist, future_best))

            memo[state] = best
            return best

        return dfs(1, m - 1, position[0])