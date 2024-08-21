from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixsum = []
        running_sum_sofar = 0

        for i in range(len(nums)):
            running_sum_sofar = running_sum_sofar + nums[i]
            prefixsum.append(running_sum_sofar)
        return prefixsum

    def runningSumWithNoextraSpace(self, nums: List[int]) -> List[int]:
        # prefixsum=[]
        running_sum_sofar = 0

        for i in range(len(nums)):
            running_sum_sofar = running_sum_sofar + nums[i]
            nums[i] = running_sum_sofar
        return nums
