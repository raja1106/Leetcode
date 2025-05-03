class Solution:
    def searchRange(self, nums, target):
        first = self.firstGreaterEqual(nums, target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        last = self.firstGreaterEqual(nums, target + 1) - 1
        return [first, last]

    def firstGreaterEqual(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid-1
            else:
                start = mid + 1
        return start


class Solution_April_2025:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # llllLRrrrr
        def find_first():  # here left is <target and right is >=target
            start = 0
            end = len(nums) - 1

            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return start

        def find_last():  # here left is <=target and right is >target
            start = 0
            end = len(nums) - 1

            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] <= target:
                    start = mid + 1
                else:
                    end = mid - 1
            return end

        first = find_first()
        if first >= len(nums) or nums[first] != target:
            return [-1, -1]
        last = find_last()
        return [first, last]
