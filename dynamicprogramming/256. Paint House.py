class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        n = len(costs)
        # For Paint House I, k is always 3 (Red, Blue, Green)
        k = len(costs[0])

        # Track the minimum, second minimum, and index of minimum from the previous house
        prev_min1, prev_idx1, prev_min2 = 0, -1, 0

        for i in range(n):
            curr_min1, curr_idx1, curr_min2 = float('inf'), -1, float('inf')

            for j in range(k):
                # If current color j matches previous best color, we must use the second best
                # otherwise, use the absolute best.
                prev_cost_to_add = prev_min2 if j == prev_idx1 else prev_min1
                cost = costs[i][j] + prev_cost_to_add

                # Standard logic to track the two smallest values in the current row
                if cost < curr_min1:
                    curr_min2 = curr_min1
                    curr_min1 = cost
                    curr_idx1 = j
                elif cost < curr_min2:
                    curr_min2 = cost

            # Update previous values for the next house
            prev_min1, prev_idx1, prev_min2 = curr_min1, curr_idx1, curr_min2

        return prev_min1