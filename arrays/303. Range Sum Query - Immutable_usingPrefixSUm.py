from typing import List


class NumArray:
    numslocal = []
    result = []

    def __init__(self, nums: List[int]):
        self.prefixsums = []
        runningsum=0
        for i in range(len(nums)):
            runningsum +=nums[i]
            self.prefixsums.append(runningsum)

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.prefixsums[right]
        return self.prefixsums[right]-self.prefixsums[left-1]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)