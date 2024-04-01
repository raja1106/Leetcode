from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: #T(n): O(n)
        stop_index = len(intervals)
        result = []
        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0]:
                stop_index = i
                break
            result.append(intervals[i])
        result.append(newInterval)

        for i in range(stop_index, len(intervals)):
            if result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1]= [min(result[-1][0],intervals[i][0]),max(result[-1][1],intervals[i][1])]

        return result

    def insertUsingSorting(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: #T(n)=O(n log n)
        intervals.append(newInterval)
        intervals.sort(key=lambda pair: pair[0])
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):

            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result

    class Solution:
        def insert(
                self, intervals: List[List[int]], newInterval: List[int]
        ) -> List[List[int]]:
            res = []

            for i in range(len(intervals)):
                if newInterval[1] < intervals[i][0]:
                    res.append(newInterval)
                    return res + intervals[i:]
                elif newInterval[0] > intervals[i][1]:
                    res.append(intervals[i])
                else:
                    newInterval = [
                        min(newInterval[0], intervals[i][0]),
                        max(newInterval[1], intervals[i][1]),
                    ]
            res.append(newInterval)
            return res
