from typing import List


class NumArray:
    numslocal = []
    result = []

    def __init__(self, nums: List[int]):
        self.numslocal = nums

    def sumRange(self, left: int, right: int) -> int:
        rangeSum = 0

        for i in range(left, right + 1):
            rangeSum = rangeSum + self.numslocal[i]

        self.result.append(rangeSum)
        return rangeSum
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)