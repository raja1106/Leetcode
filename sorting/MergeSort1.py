from typing import List
class MergeSort1:
    def sort(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums,0,len(nums)-1)

    def mergesort(self,nums: List[int],start: int,end: int) -> List[int]:
        if start == end:
            return [nums[start]]

        mid = start+(end-start)//2
        left  = self.mergesort(nums,start,mid)
        right = self.mergesort(nums,mid+1,end)
        return self.merge(left,right)

    def merge(self,left: List[int],right: List[int]) -> List[int]:
        i,j = 0,0
        result=[]  #1,3,5      2,4,6,8
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result


sort = MergeSort1()
print(sort.sort([4,6,1,2,3,5]))

