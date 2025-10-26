class Solution_Best_Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # Sorting takes O(N log N)
        n = len(nums)

        for i in range(n):
            # Skip duplicate elements for 'i'
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            left, right = i + 1, n - 1
            target = -nums[i]

            while left < right:
                combined_value = nums[left] + nums[right]
                if combined_value == target:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate values for left and right pointers
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif combined_value < target:
                    left += 1
                else:
                    right -= 1
        return result

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

    def threeSumWithoutUsingSet(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            target = -nums[i]

            while left < right:
                combined_value = nums[left]+nums[right]
                if combined_value == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left, right = left + 1, right - 1
                    # Skip duplicate elements by moving the left pointer to the right.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicate elements by moving the right pointer to the left.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif combined_value < target:
                    left += 1
                else:
                    right -= 1

        return result


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


class Solution_Without_Sorting:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set = set()  # To store unique triplets
        seen = set()  # To avoid processing the same number again for 'i'

        # Iterate through the array, treating each element as the first element of the triplet
        for i in range(len(nums)):
            if nums[i] in seen:  # Skip if we have already processed this number for 'i'
                continue
            seen.add(nums[i])
            target = -nums[i]  # We are looking for two numbers that sum to -nums[i]
            complements = set()  # To store numbers that we have seen in the current pass
            for j in range(i + 1, len(nums)):
                complement = target - nums[j]  # The number we need to form a triplet
                if complement in complements:
                    # If the complement is found, we have a valid triplet
                    result_set.add(tuple(sorted([nums[i], nums[j], complement])))
                complements.add(nums[j])  # Add the current number to the complement set

        # Convert the set of tuples into a list of lists for the final result
        return list(result_set)
