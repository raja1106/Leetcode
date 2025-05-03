from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        left = right = 0

        for left in range(len(arr) - 1):
            if arr[left] >= arr[left + 1]:
                break

        for right in range(len(arr) - 1, 0, -1):
            if arr[right - 1] <= arr[right]:
                break

        if left == right:
            return True
        else:
            return False


