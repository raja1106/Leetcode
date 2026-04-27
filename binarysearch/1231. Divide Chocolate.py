from typing import List
import math


class Solution_Best:
    '''
llllllllLRrrrrrrrrr
left region --> possible to have k+1 pieces
right region --> not possible to have k+1 pieces
returns 'L' which is 'end'
    '''
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        def can_be_cut(target_sweetness):
            count = 0
            current_sweetness = 0
            for val in sweetness:
                current_sweetness += val
                if current_sweetness >= target_sweetness:
                    count += 1
                    current_sweetness = 0
            return count >= (k + 1)

        start = 1
        end = sum(sweetness)

        while start <= end:
            mid = start + (end - start) // 2
            if can_be_cut(mid):
                start = mid + 1  # mid is feasible, try higher
            else:
                end = mid - 1  # mid too greedy, go lower

        return end

class Solution_Bruteforce:
    def maximizeSweetnessBruteforce(self, sweetness: List[int], k: int) -> int:
        n = len(sweetness)
        best_min_sweetness = 0

        def dfs(start_index: int, cuts_left: int, min_so_far: int) -> None:
            nonlocal best_min_sweetness

            if cuts_left == 0:
                last_piece_sum = sum(sweetness[start_index:])
                final_min = min(min_so_far, last_piece_sum)
                best_min_sweetness = max(best_min_sweetness, final_min)
                return

            current_sum = 0

            for end_index in range(start_index, n - cuts_left):
                current_sum += sweetness[end_index]
                dfs(end_index + 1, cuts_left - 1, min(min_so_far, current_sum))

        dfs(0, k, math.inf)
        return best_min_sweetness