from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = {}
        first = {}
        last = {}

        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i
            last[x] = i
            count[x] = count.get(x, 0) + 1

        degree = max(count.values())

        best_len = float('inf')
        for x, c in count.items():
            if c == degree:
                best_len = min(best_len, last[x] - first[x] + 1)

        return best_len


class Solution_naive_way:
    def findShortestSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        count_map = defaultdict(list)
        max_freq = 1
        for i in range(len(nums)):
            count_map[nums[i]].append(i)

        for k, v in count_map.items():
            if len(v) > max_freq:
                max_freq = len(v)
        result_val = float('inf')
        for k, v in count_map.items():
            if len(v) == max_freq:
                result_val = min(result_val, v[-1] - v[0] + 1)

        return result_val


class Solution_Algo_Monster:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Count frequency of each number in the array
        frequency_map = Counter(nums)

        # Find the degree (maximum frequency) of the array
        max_frequency = frequency_map.most_common()[0][1]

        # Track first and last occurrence index for each number
        first_occurrence = {}
        last_occurrence = {}

        # Iterate through array to record first and last positions
        for index, value in enumerate(nums):
            if value not in first_occurrence:
                first_occurrence[value] = index
            last_occurrence[value] = index

        # Initialize minimum length to infinity
        min_length = float('inf')

        # Check each number to find shortest subarray with same degree
        for value in nums:
            # Only consider numbers that have the maximum frequency
            if frequency_map[value] == max_frequency:
                # Calculate subarray length from first to last occurrence
                subarray_length = last_occurrence[value] - first_occurrence[value] + 1
                # Update minimum length if current is shorter
                if min_length > subarray_length:
                    min_length = subarray_length

        return min_length