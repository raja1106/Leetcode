# example  2,3,4,7,None,None --> 2,2,3
import math
from typing import List


class Solution1:
    def solution(self, nums: List[int]) -> List[int]:
        right = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == None:
                continue

            if nums[i] % 2 == 0:
                nums[right] = nums[i]
                right -= 1
                nums[right] = nums[i]
                right -= 1
            else:
                nums[right] = nums[i]
                right -= 1
        return nums

    def solution1(self, nums: List[int]) -> List[int]:
        start,end = 0,len(nums)-1
        result_index=len(nums)-1
        result=[0]*len(nums)

        while(start <= end):
            print(start)
            print("end")
            print(end)
            if abs(nums[start]) > abs(nums[end]):
                result[result_index] = nums[start] * nums[start]
                start += 1
            else:
                result[result_index] = nums[end] * nums[end]
                end -=1

            result_index -= 1

        return result

obj1= Solution1()
nums=[-12,3,4,7,9]
result = obj1.solution1(nums)
print(result)