from typing import List
class BubbleSort:
    def bubbleSort(self, array: List[int]) -> List[int]:

        for i in range(len(array)):
            for j in range(len(array) - 1, i, -1):
                if array[j - 1] > array[j]:
                    array[j - 1], array[j] = array[j], array[j - 1]
        return array



sort = BubbleSort()
print(sort.bubbleSort([4,-6,1,2,3,-5]))
