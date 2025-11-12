from typing import List

from heapq import heappush, heappop

from heapq import heapify, heappush, heappop


class Solution_Min_heap:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []

        for i, v in enumerate(arr):
            abs_val = abs(v - x)
            heappush(min_heap, (abs_val, i))

        result = []

        for i in range(k):
            idx = heappop(min_heap)[1]
            result.append(arr[idx])

        result.sort()
        return result

class Solution_Using_Max_Heap: # Not efficient one.. But understandable
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []

        for num in arr:
            diff = abs(num - x)
            heappush(max_heap, (-diff, -num))  # Use negative to simulate max-heap in min-heap structure
            if len(max_heap) > k:
                heappop(max_heap)

        result = sorted([-num for _, num in max_heap])  # Convert back from negative values
        return result

class Solution_Best_Binary_search:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Binary search for the best starting index of the window
        start = 0
        end = len(arr) - k

        while start <= end:
            mid = (start + end) // 2
            # Compare distances to decide direction
            if mid+k < len(arr) and x - arr[mid] > arr[mid + k] - x:
                start = mid + 1  # Shift window to the end
            else:
                end = mid-1  # Shift window to the start

        return arr[start:start + k]

class Solution_Using_linear: #O(n) time complexity
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left,right = 0, len(arr)-1
        to_remove = len(arr)-k
        while to_remove!=0:
            diff_1 = abs(x-arr[left])
            diff_2 = abs(x-arr[right])
            if diff_1 <= diff_2:
                right -= 1
            else:
                left += 1
            to_remove -= 1
        return arr[left:right+1]

class Solution_Understandable_one:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start, end = 0, len(arr) - 1
        """
        lllllLRrrrrr
        start = 0
        end = n-1
        """
        # Binary search to find the closest value to x
        closest_value, closest_index = arr[0], 0
        while start <= end:
            mid = (start + end) // 2
            current_diff = abs(arr[mid] - x)
            closest_diff = abs(closest_value - x)

            # Update the closest value and index if necessary
            if current_diff < closest_diff or (current_diff == closest_diff and arr[mid] < closest_value):
                closest_value, closest_index = arr[mid], mid

            # Adjust the binary search range
            if arr[mid] < x:
                start = mid + 1
            elif arr[mid] > x:
                end = mid - 1
            else:
                break
        # Initialize the window around the closest index
        start = end = closest_index
        # Expand the window to include k elements
        for _ in range(k - 1):
            if start == 0:
                end += 1
            elif end == len(arr) - 1 or x - arr[start - 1] <= arr[end + 1] - x:
                start -= 1
            else:
                end += 1
        # Return the k closest elements
        return arr[start:end + 1]


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize the left and end pointers for binary search.
        # The end pointer is set to the highest possible starting index for the sliding window of size k.
        start, end = 0, len(arr) - k

        # Perform binary search to find the left bound of the k closest elements.
        while start < end:
            # Calculate the middle index between left and end.
            mid = (start + end) // 2
            # Check the distances to x from the mid element and the element at mid + k position.
            # If the element at mid is closer to x or equally distant compared to the element at mid + k,
            # move the end pointer to mid. Otherwise, move the left pointer to mid + 1.
            if x - arr[mid] <= arr[mid + k] - x:
                end = mid
            else:
                start = mid + 1

        # The subarray starting at index left of size k will be the k closest elements.
        return arr[start:start + k]
def run_tests():
    solution = Solution()

    # Test Case 1: Basic Case
    solution.findClosestElements([1, 2, 3, 4, 5], 4, 3)

    # Test Case 2: Element Not Present in Array
    solution.findClosestElements([1, 3, 5, 7, 9], 3, 4)

    # Test Case 3: x Less Than All Elements
    solution.findClosestElements([10, 20, 30, 40, 50], 2, 5)

    # Test Case 4: x Greater Than All Elements
    assert solution.findClosestElements([10, 20, 30, 40, 50], 3, 60) == [30, 40, 50], "Test Case 4 Failed"

    # Test Case 5: k Equal to Array Length
    assert solution.findClosestElements([1, 2, 3, 4, 5], 5, 3) == [1, 2, 3, 4, 5], "Test Case 5 Failed"

    # Test Case 6: x Exactly at the Start of the Array
    assert solution.findClosestElements([1, 2, 3, 4, 5], 3, 1) == [1, 2, 3], "Test Case 6 Failed"

    # Test Case 7: x Exactly at the End of the Array
    assert solution.findClosestElements([1, 2, 3, 4, 5], 2, 5) == [4, 5], "Test Case 7 Failed"

    # Test Case 8: All Elements Are the Same
    assert solution.findClosestElements([2, 2, 2, 2, 2], 3, 2) == [2, 2, 2], "Test Case 8 Failed"

    # Test Case 9: x in the Middle of the Array
    assert solution.findClosestElements([1, 3, 5, 7, 9], 2, 6) == [5, 7], "Test Case 9 Failed"

    # Test Case 10: Large k but Small Array
    assert solution.findClosestElements([10, 20, 30], 2, 15) == [10, 20], "Test Case 10 Failed"

    # Test Case 11: Small k with a Large Array
    assert solution.findClosestElements([1, 10, 15, 20, 25, 30], 1, 18) == [20], "Test Case 11 Failed"

    # Test Case 12: Very Large k (close to the array size)
    assert solution.findClosestElements([10, 20, 30, 40, 50], 4, 35) == [20, 30, 40, 50], "Test Case 12 Failed"

    print("All test cases passed!")

# Run the tests
run_tests()

