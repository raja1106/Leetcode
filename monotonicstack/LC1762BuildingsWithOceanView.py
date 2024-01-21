from typing import List
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
         st=[]
         for i in range(len(heights)):
             while st and st[-1][0] <= heights[i]:
                 st.pop()
             st.append((heights[i],i))
         result=[]
         for i in range(len(st)):
             result.append(st[i][1])
         return result