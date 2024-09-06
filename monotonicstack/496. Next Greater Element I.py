from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        next_greater_map = {}

        for i in range(len(nums2) - 1, -1, -1):
            print(nums2[i])
            while st and st[-1] <= nums2[i]:
                st.pop()
            if st:
                next_greater_map[nums2[i]] = st[-1]
            else:
                next_greater_map[nums2[i]] = -1
            st.append(nums2[i])

        ans = []
        for num in nums1:
            ans.append(next_greater_map[num])
        return ans