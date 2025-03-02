from typing import List


class Solution:

    def findMaxAverage_BestWay(self, nums: List[int], k: int) -> float:
        # Initial sum of the first 'k' elements
        current_sum = sum(nums[:k])
        # Starting with the initial sum as the max sum
        max_sum = current_sum

        # Iterate over the list starting from the k-th element to the end
        for i in range(k, len(nums)):
            # Update the current sum by adding the next element and
            # subtracting the (i-k)-th element, sliding the window forward
            current_sum += nums[i]
            current_sum -= nums[i - k]
            # Update the max sum if the current sum is greater
            max_sum = max(max_sum, current_sum)

        # Calculate the maximum average by dividing the max sum by k
        return max_sum / k
    def findMaxAverageBruteforceWay(self, nums: List[int], k: int) -> float:

        if len(nums) <= k:
            return float(sum(nums) / len(nums))

        q = [0] * k

        for i in range(k):
            q[i] = nums[i]
        maxaverage = float(sum(q) / k)
        test = len(nums) - k
        for j in range(k, len(nums)):
            q.pop(0) #O(n) here.. if we use deque then it is O(1)
            q.append(nums[j])
            maxaverage = max(maxaverage, float(sum(q) / k))
        return maxaverage

    def findMaxAverage(self, nums: List[int], k: int) -> float:

        if len(nums) <= k:
            return float(sum(nums) / len(nums))

        q = [0] * k

        for i in range(k):
            q[i] = nums[i]
        windowsum = sum(q)
        maxtotal=windowsum
        for j in range(k, len(nums)):
            windowsum -= q.pop(0)
            windowsum +=nums[j]
            q.append(nums[j])
            maxtotal = max(maxtotal, windowsum)
        return float(maxtotal / k)


