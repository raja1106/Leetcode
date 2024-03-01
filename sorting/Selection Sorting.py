from typing import List
class SelectionSort:
    def sort(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            min_index =i
            for j in range(i+1,len(nums)):
                if nums[j] < nums[min_index]:
                    min_index =j
            nums[min_index],nums[i]=nums[i],nums[min_index]
        return nums


sort =SelectionSort()
print(sort.sort([4,6,1,0,6,2,3,-5]))
