from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i,j =0,0
        result=[]
        while i<len(firstList) and j<len(secondList):
            if firstList[i][1] < secondList[j][0]:
                i += 1
            elif firstList[i][0] > secondList[j][1]:
                j +=1
            else:
                result.append([max(firstList[i][0],secondList[j][0]),min(firstList[i][1],secondList[j][1])])
                if firstList[i][1] < secondList[j][1]:
                    i +=1
                else:
                    j +=1

        return result

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:#This is not working
        merged_list = []
        merged_list.extend(firstList)
        merged_list.extend(secondList)
        merged_list.sort(key=lambda x:x[0])

        result = []

        for i in range(len(merged_list)-1):
            if merged_list[i][1] >= merged_list[i+1][0]:
                result.append([merged_list[i+1][0],merged_list[i][1]])

        return result




