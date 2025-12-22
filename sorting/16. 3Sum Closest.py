from typing import List

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Finds three integers in nums such that the sum is closest to target.
        """
        # Edge case: If fewer than 3 numbers, we cannot form a triplet.
        # (Though problem constraints usually guarantee len >= 3)
        if len(nums) < 3:
            raise ValueError("Input array must contain at least three integers.")

        # Sorting is crucial to use the Two-Pointer approach effectively.
        nums.sort()

        # Initialize closest_sum with the first valid triplet to have a baseline.
        closest_sum = nums[0] + nums[1] + nums[2]
        n = len(nums)

        # Iterate through the array, fixing one number (nums[i]) at a time.
        for i in range(n - 2):
            # Optional Optimization: Skip duplicate 'i' values to save computation
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find the best pair for the fixed nums[i]
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # If we found an exact match, the difference is 0, so return immediately.
                if current_sum == target:
                    return target

                # Update closest_sum if the current one is closer to target
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                # Move pointers based on comparison to target
                if current_sum < target:
                    # We need a larger sum, so move the left pointer to the right
                    left += 1
                else:
                    # We need a smaller sum, so move the right pointer to the left
                    right -= 1

        return closest_sum

class Solution_Optimized_with_Pruning:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        best = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            # Skip duplicate anchors to reduce work
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # ---- Pruning using min/max possible sums for this i ----
            min_sum = nums[i] + nums[i + 1] + nums[i + 2]
            if min_sum > target:
                # since i increases => min_sum will only increase; we can stop
                if abs(min_sum - target) < abs(best - target):
                    best = min_sum
                break

            max_sum = nums[i] + nums[n - 2] + nums[n - 1]
            if max_sum < target:
                # even the largest is still below target; move to next i
                if abs(max_sum - target) < abs(best - target):
                    best = max_sum
                continue

            # ---- Normal two-pointer search ----
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if abs(s - target) < abs(best - target):
                    best = s

                if s == target:
                    return target
                elif s < target:
                    left += 1
                else:
                    right -= 1

        return best

from typing import List

class Solution_initial_way:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        closest_sum = nums[0] + nums[1] + nums[2]
        closest_distance = abs(closest_sum - target)

        for i in range(n - 2):
            new_target = target - nums[i]

            left = i + 1
            right = n - 1

            while left < right:
                pair_sum = nums[left] + nums[right]
                current_sum = nums[i] + pair_sum
                dist = abs(current_sum - target)

                if dist < closest_distance:
                    closest_distance = dist
                    closest_sum = current_sum

                if pair_sum == new_target:
                    return target  # exact match
                elif pair_sum < new_target:
                    left += 1
                else:
                    right -= 1

        return closest_sum