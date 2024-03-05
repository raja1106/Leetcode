from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result =[]

        set1 =set(nums1)

        for i in range(len(nums2)):
            if nums2[i] in set1:
                result.append(nums2[i])
                set1.remove(nums2[i])

        return result

    def intersection_Algo_monster(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert the first list to a set to eliminate duplicates
        set_nums1 = set(nums1)

        # Convert the second list to a set to eliminate duplicates
        set_nums2 = set(nums2)

        # Find the intersection of the two sets, which contains only the common elements
        intersection_set = set_nums1 & set_nums2

        # Convert the resulting set to a list before returning
        return list(intersection_set)