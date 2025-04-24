class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority_candidate = None

        # Process each number in the list
        for num in nums:
            # If the current count is 0, we choose a new number as the potential majority candidate
            if count == 0:
                majority_candidate = num
                count = 1
            # If the current number is the same as the majority candidate, increase the count
            elif majority_candidate == num:
                count += 1
            # Otherwise, decrease the count
            else:
                count -= 1

        # Verify if the candidate is actually the majority element
        if nums.count(majority_candidate) > len(nums) // 2:
            return majority_candidate
        else:
            return -1  # Indicate no majority element


class Solution_Using_Map:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = Counter(nums)

        for k, v in count_map.items():
            if v > len(nums) // 2:
                return k

        return -1

class Solution_using_most_common:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = Counter(nums).most_common(1)[0]
        return candidate if count > len(nums) // 2 else -1
