class Solution_Feb_2024:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        for i in range(len(nums)):
            while i != nums[i] - 1:  # i = 1, we have 5
                d = nums[i] - 1  # d = 4
                if  0 <= d < len(nums) and nums[i] != nums[d]:
                    swap(i, d)
                else:
                    break

        for i in range(len(nums)):
            if i != nums[i] - 1:
                return i + 1

        return len(nums) + 1

class Solution_Old:
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



