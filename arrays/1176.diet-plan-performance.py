from typing import List


class Solution:
    def dietPlanPerformance_mycode(self, calories: List[int], k: int, lower: int, upper: int) -> int:

        result = 0
        total = 0
        nums = calories
        for i in range(k):
            total += nums[i]

        if total > upper:
            result += 1
        if total < lower:
            result -= 1

        for i in range(k, len(calories)):
            total += calories[i]
            total -= calories[i - k]
            if total > upper:
                result += 1
            if total < lower:
                result -= 1

        return result

class Solution_AlgoMonster:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        # Helper function to evaluate the points for the given sum of calories
        def evaluate_points(calories_sum):
            # If the sum is less than the lower bound, return -1 point
            if calories_sum < lower:
                return -1
            # If the sum is greater than the upper bound, return 1 point
            elif calories_sum > upper:
                return 1
            # Otherwise, no points are awarded or deducted
            else:
                return 0

        # Calculate the initial sum of the first 'k' elements
        sliding_window_sum = sum(calories[:k])
        # Initialize score with the points from initial sum
        score = evaluate_points(sliding_window_sum)
        # Length of the calories list
        n = len(calories)

        # Iterate over the remaining elements, updating the sum and score
        for i in range(k, n):
            # Update the sliding window sum by adding the current element and removing the oldest one
            sliding_window_sum += calories[i] - calories[i - k]
            # Update the score based on the updated sum
            score += evaluate_points(sliding_window_sum)

        # Return the total score after evaluating all sliding windows
        return score