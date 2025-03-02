# Definition for an Interval.

class Solution_Feb_2024:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        all_intervals = []
        # Flatten the list of intervals
        for employee_intervals in schedule:
            all_intervals.extend(employee_intervals)
        # Sort all intervals by start time
        all_intervals.sort(key=lambda interval: interval.start)
        merged_intervals = [all_intervals[0]]
        # Merge overlapping intervals
        for interval in all_intervals:
            if merged_intervals[-1].end >= interval.start:
                merged_intervals[-1].end = max(merged_intervals[-1].end, interval.end)
            else:
                merged_intervals.append(interval)  # Add non-overlapping interval

        free_time_intervals = []
        # Identify gaps between merged intervals as free time
        for i in range(len(merged_intervals) - 1):
            free_time_intervals.append(Interval(merged_intervals[i].end, merged_intervals[i + 1].start))

        return free_time_intervals  # Returns a list of Interval objects representing free time


class Solution__Feb_2024_Using_MinHeap:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        min_heap = []
        # Push the first interval of each employee's schedule into the heap
        for i, employee_intervals in enumerate(schedule):
            if employee_intervals:
                heappush(min_heap, (employee_intervals[0].start, employee_intervals[0].end, i, 0))
        merged_intervals = []
        # Process intervals from the heap
        while min_heap:
            start, end, employee_index, interval_index = heappop(min_heap)
            # Merge overlapping intervals
            if merged_intervals and merged_intervals[-1].end >= start:
                merged_intervals[-1].end = max(merged_intervals[-1].end, end)
            else:
                merged_intervals.append(Interval(start, end))
            # Push the next interval from the same employee's schedule
            next_index = interval_index + 1
            if next_index < len(schedule[employee_index]):
                next_interval = schedule[employee_index][next_index]
                heappush(min_heap, (next_interval.start, next_interval.end, employee_index, next_index))
        free_time_intervals = []
        # Identify gaps between merged intervals as free time
        for i in range(len(merged_intervals) - 1):
            free_time_intervals.append(Interval(merged_intervals[i].end, merged_intervals[i + 1].start))
        return free_time_intervals



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



