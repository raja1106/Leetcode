from typing import List
from collections import Counter

class Solution:

    def arrays_intersection_ALgomonster(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # Create a counter object which will store the frequency of each number across all three arrays
        elements_count = Counter(arr1 + arr2 + arr3)

        # Find the intersection by checking which numbers have a count equal to 3 - meaning they appear in all three arrays
        intersection = [number for number in arr1 if elements_count[number] == 3]
        """
        Below lines are same as "intersection = [number for number in arr1 if elements_count[number] == 3]"
        result = []
    
        for i,v in enumerate(arr1):
            if v in elements_count and elements_count[v] == 3:
                result.append(v)
        :return result        
        """
        # Return the list of numbers that are present in all three arrays
        return intersection


