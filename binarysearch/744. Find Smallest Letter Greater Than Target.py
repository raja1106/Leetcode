from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters) - 1

        """
                - - - - - t - - - - 
                <= is left region
                > is right region
                my plan is to move start into right region and end into left region
                by that way I will get "start" is the correct ans
                if start is len(nums), then return 0
        """

        while start <= end:
            mid = start + (end - start) // 2
            if letters[mid] <= target:
                start = mid + 1
            elif letters[mid] > target:
                end = mid - 1

        return letters[start % len(letters)]
