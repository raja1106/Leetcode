class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left=0
        max_sum=-1
        window_sum=0
        window_set=set()
        for i in range(len(nums)):
            window_sum += nums[i]

            while left<i and nums[i] in window_set:
                window_set.remove(nums[left])
                window_sum -= nums[left]
                left += 1

            window_set.add(nums[i])
            max_sum = max(max_sum,window_sum)
        
        return max_sum