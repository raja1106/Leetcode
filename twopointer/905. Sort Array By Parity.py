class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        next_even_number = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[next_even_number] = nums[next_even_number], nums[i]
                next_even_number += 1

        return nums
