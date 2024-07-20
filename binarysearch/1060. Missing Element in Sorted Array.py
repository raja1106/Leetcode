class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # 4,7,9,10   k=3, ans=8
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            actual_val = nums[mid]
            predicted_val = nums[0] + mid
            missing = actual_val - predicted_val
            if missing < k:
                start = mid + 1
            else:
                end = mid - 1
        missing = nums[end] - (nums[0] + end)
        return nums[end]+(k-missing)
