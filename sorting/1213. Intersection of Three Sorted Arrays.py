from typing import List
from collections import Counter
from collections import deque

class Solution:

    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # Time Complexity: O(n)
        i=j=k=0
        result= []
        while i<len(arr1) and j<len(arr2) and k<len(arr3):
            min_val = min(arr1[i], arr2[j], arr3[k])
            if arr1[i] == arr2[j] == arr3[k]:
                result.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif arr1[i] == min_val:
                i += 1
            elif arr2[j] == min_val:
                j += 1
            else:
                k += 1
        return result

    def arrays_intersection_UsingHashTable(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        #Time Complexity: O(n)
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


