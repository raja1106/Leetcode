class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=set()
        nums.sort()
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            target = -nums[i]

            while left < right:
                combined_value = nums[left]+nums[right]
                if combined_value == target:
                    result.add((nums[i],nums[left],nums[right]))
                    left += 1
                elif combined_value < target:
                    left += 1
                else:
                    right -= 1

        return list(result)


    def threeSum_m(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=set()
        nums.sort()

        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            target = -nums[i]

            self.twoSum(i, left, nums, result, right, target)

        return list(result)

    def twoSum(self, i, left, nums, result, right, target):
        while left < right:
            combined_value = nums[left] + nums[right]
            if combined_value == target:
                result.add((nums[i], nums[left], nums[right]))
                left += 1
            elif combined_value < target:
                left += 1
            else:
                right -= 1