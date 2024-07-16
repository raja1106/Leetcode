from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <3:
            return False

        start=0
        end=len(arr)
        leftPeakElement=-1
        rightPeakELement=-1
        for i in range(1,len(arr)):
            if arr[i-1] < arr[i] > arr[i+1]:
                leftPeakElement =i
                break

        for j in range(len(arr)-2,0,-1):
            if arr[j-1] < arr[j] > arr[j+1]:
                rightPeakELement =j
                break

        if  leftPeakElement == rightPeakELement:
            return True
        else:
            return False


