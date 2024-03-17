'''
378. Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
'''

from typing import List
from heapq import heappop,heapify,heappush


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []

        for row in matrix:
            min_heap.extend(row)

        heapify(min_heap)

        for i in range(k-1):
            heappop(min_heap)

        return heappop(min_heap)

    def kthSmallest_Mons(self, matrix: List[List[int]], k: int) -> int: #TODOO understand this solution
        # Helper function to count the number of elements smaller or equal to mid
        def count_less_equal(mid, k, size):
            count = 0
            row, col = size - 1, 0  # Start with the bottom-left corner of the matrix

            while row >= 0 and col < size:
                if matrix[row][col] <= mid:
                    count += row + 1  # Add all the elements of the current column
                    col += 1  # Move to the next column
                else:
                    row -= 1  # Move to the previous row

            return count >= k  # Check if the count is greater than or equal to k

        size = len(matrix)
        # Set initial binary search bounds
        left, right = matrix[0][0], matrix[size - 1][size - 1]

        # Perform binary search
        while left < right:
            mid = (left + right) // 2  # Choose the middle value
            # If the count of numbers less than or equal to mid is k or more
            if count_less_equal(mid, k, size):
                right = mid  # Narrow down the search space to the lower half
            else:
                left = mid + 1  # Narrow down the search space to the upper half

        return left  # The kth smallest number






























