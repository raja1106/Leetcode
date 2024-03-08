from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):

            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result


obj = Solution()
print(obj.merge([[1,3],[2,6],[8,10],[15,18]]))