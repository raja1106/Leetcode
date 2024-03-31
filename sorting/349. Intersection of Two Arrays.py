from typing import List
"""
Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result =[]

        set1 =set(nums1)

        for i in range(len(nums2)):
            if nums2[i] in set1:
                result.append(nums2[i])
                set1.remove(nums2[i])

        return result

    def intersection_no_extraspace(self, nums1: List[int], nums2: List[int]) -> List[int]:#T(n) = O (max(nlogn,mlogm)
        ans = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                # ans.append(nums1[i]) # for Leetcode 350, input with duplicates
                if (not ans) or (len(ans) > 0 and ans[-1] != nums1[i]):
                    ans.append(nums1[i])
                i += 1
                j += 1

        return ans

    def intersection_Algo_monster(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert the first list to a set to eliminate duplicates
        set_nums1 = set(nums1)

        # Convert the second list to a set to eliminate duplicates
        set_nums2 = set(nums2)

        # Find the intersection of the two sets, which contains only the common elements
        intersection_set = set_nums1 & set_nums2

        # Convert the resulting set to a list before returning
        return list(intersection_set)

    """
    Time Complexity
The time complexity for the given solution involves two main operations: converting the lists to sets and finding the intersection of these sets.

Converting nums1 to a set: This operation has a time complexity of O(n) where n is the number of elements in nums1.
Converting nums2 to a set: Similarly, this has a time complexity of O(m) where m is the number of elements in nums2.
Finding the intersection: The intersection operation & for sets is normally O(min(n, m)) because it checks each element in the smaller set for presence in the larger set.
Thus, the overall time complexity can be summarized as O(max(n, m)) assuming that the intersection operation is dominated by the process of converting the lists to sets.
    """