from typing import List
class InsertionSort:
    def sort(self, nums: List[int]) -> List[int]:
        if len(nums) <=1:
            return nums

        for i in range(len(nums)):
            temp = nums[i]
            j=i-1
            while j>=0 and nums[j] > temp:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = temp
        return nums


sort =InsertionSort() # 0, 1, 2, 3, 3, 4, 6,6
print(sort.sort([4,6,1,0,6,2,3,-5]))
