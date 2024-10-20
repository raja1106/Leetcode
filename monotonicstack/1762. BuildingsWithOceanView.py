from typing import List

'''
        #if you can't decide without looking into all the the info in the right direction.. 
        so coming from n-1 to 0 is natural way
'''

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        st = []
        for i in range(len(heights)):
            while st and st[-1][0] <= heights[i]:
                st.pop()
            st.append((heights[i], i))
        result = []
        for i in range(len(st)):
            result.append(st[i][1])
        return result
class Solution_Another_Approach:
    def findBuildings(self, heights: List[int]) -> List[int]:
        #[6,2,3,5].  [6,5] 6 , 5, 4
        n= len(heights)
        ans = []
        max_height_so_far = -1
        for i in range(n-1,-1,-1):
            if heights[i] > max_height_so_far:
                ans.append(i)
            max_height_so_far = max(max_height_so_far,heights[i])
        ans.reverse()
        return ans
