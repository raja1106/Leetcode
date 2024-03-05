from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        result = []

        while i < len(nums1) and j < len(nums2):

            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result

    def intersect_AlgoMonster(self, nums1: List[int], nums2: List[int]) -> List[int]:

        element_counter = Counter(nums1)

        intersection_result = []

        for num in nums2:
            # If the current element is present in the element counter
            # and the count is more than 0, it's part of the intersection.
            if element_counter[num] > 0:
                # Append the element to the result list
                intersection_result.append(num)

                # Decrement the count of the current element in the counter
                element_counter[num] -= 1

        # Return the final list of intersection elements
        return intersection_result

