class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_length = len(nums)
        for i in range(nums_length):
            while 0 <= nums[i] - 1 < nums_length and i + 1 != nums[i]:
                target_index = nums[i] - 1
                if nums[target_index] != nums[i]:
                    nums[i], nums[target_index] = nums[target_index], nums[i]
                else:
                    break
        for i in range(nums_length):
            if i + 1 != nums[i]:
                return i + 1

        return nums_length + 1
