# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Flattening the schedule
        intervals = [interval for employee in schedule for interval in employee]
        # Sorting by start of each Interval
        intervals.sort(key=lambda x: x.start)
        res, end = [], intervals[0].end
        # Checking for free time between intervals
        for i in intervals[1:]:
            if end < i.start:
                res.append(Interval(end, i.start))
            end = max(end, i.end)
        return res

class Solution1:
  def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
    ans = []
    intervals = []

    for s in schedule:
      intervals.extend(s)

    intervals.sort(key=lambda x: x.start)

    prevEnd = intervals[0].end


    for interval in intervals:
      if interval.start > prevEnd:
        ans.append(Interval(prevEnd, interval.start))
      prevEnd = max(prevEnd, interval.end)

    return ans

  def employeeFreeTime_March31(self, schedule: '[[Interval]]') -> '[Interval]':
      sorted_schedule=[]
      for interval in schedule:
          sorted_schedule.append(interval)

      sorted_schedule.sort(key=lambda interval:interval.start)
      result=[sorted_schedule[0]]

      return result



