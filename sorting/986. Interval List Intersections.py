from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        merged_list = []
        merged_list.extend(firstList)
        merged_list.extend(secondList)
        merged_list.sort(key=lambda x:x[0])

        result = []

        for i in range(len(merged_list)-1):
            if merged_list[i][1] >= merged_list[i+1][0]:
                result.append([merged_list[i+1][0],merged_list[i][1]])

        return result


