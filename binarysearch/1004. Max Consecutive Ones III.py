class Solution_Using_Sliding_Window:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        longest_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1

            while left <= i and zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            longest_length = max(longest_length, i - left + 1)

        return longest_length

class Solution_BinarySearch:  # O(n log n)
    def longestOnes(self, nums: List[int], k: int) -> int:
        # prefix_zeros[i] = number of zeros in nums[0:i]
        prefix_zeros = [0]
        for value in nums:
            prefix_zeros.append(prefix_zeros[-1] + (1 if value == 0 else 0))

        n = len(nums)
        longest_window = 0

        # Try each left boundary
        for left in range(n):
            start = left
            end = n - 1
            best_right = left - 1  # if no valid right idx found

            # Binary search using the template style
            while start <= end:
                mid = start + (end - start) // 2

                zeros_in_window = prefix_zeros[mid + 1] - prefix_zeros[left]

                if zeros_in_window <= k:
                    best_right = mid           # valid window
                    start = mid + 1            # try expanding right
                else:
                    end = mid - 1              # shrink right

            window_size = best_right - left + 1
            if window_size > longest_window:
                longest_window = window_size

        return longest_window

