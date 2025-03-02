class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        valid_subarrays = 0
        remainder_count = Counter()
        remainder_count[0] = 1
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum%k in remainder_count:
                valid_subarrays += remainder_count[prefix_sum%k]
            remainder_count[prefix_sum%k] += 1
        return valid_subarrays