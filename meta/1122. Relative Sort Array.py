from typing import List


class Solution_Using_Counting_Sort:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Find the maximum value in arr1 to determine the size of the count array
        max_val = max(arr1)

        # Initialize a count array to store frequencies
        count = [0] * (max_val + 1)

        # Populate the count array with frequencies of each number in arr1
        for num in arr1:
            count[num] += 1

        # List to store the result
        result = []

        # Add elements to result according to the order in arr2
        for num in arr2:
            result.extend([num] * count[num])
            count[num] = 0  # Set to 0 as those elements are already used

        # Add the remaining elements not in arr2, in sorted order
        for num in range(max_val + 1):
            if count[num] > 0:
                result.extend([num] * count[num])

        return result


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_freq = Counter(arr1)

        result = []

        for num in arr2:
            freq = count_freq[num]
            result.extend([num]*freq)
            del count_freq[num]
        for k,v in sorted(count_freq.items()):
            result.extend([k]*v)
        return result