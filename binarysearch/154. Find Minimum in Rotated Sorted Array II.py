class Solution:
    """
        Input: nums = [4,5,6,7,0,1,2]
        Output: 0

            left region denotes --> orange region elements(these are rotated or modified from original sorted location or corrupted so orange color)
            right region denotes --> green region elements (these are not rotated. so first element in the right region is min element of this rotated array)
            from the right region, we are returning "R", and that is "start"

            llllllllllRrrrrrrrrr
            'R' --> this 'R' we are trying to find. 'R' which is "starting of the right region". As any Binary Search Problem,
            here we are moving "start" pointer to "right region" and moving "end" pointer to "left region".
            After every iteration in while loop, we are reducing search region by n/2. so T(n) is log(n)


        """
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:  # Array is already sorted
            return nums[0]

        start = 0
        end = len(nums) - 1

        # Skip duplicates at the beginning
        while start < end and nums[start] == nums[end]:
            start += 1

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[-1]:  # middle element is in orange(left) region. So we need to move start to mid+1. we don't have any interest in elements upto mid
                start = mid + 1
            else:  # here middle element is in green region. so we are moving end to (mid-1)
                end = mid - 1

        return nums[start]