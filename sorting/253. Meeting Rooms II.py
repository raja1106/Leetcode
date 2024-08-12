
from heapq import heappop, heappush
from typing import List

class Solution1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])

        # Initialize the heap with the end time of the first meeting
        min_heap = []
        heappush(min_heap, intervals[0][1])

        # Iterate over the remaining intervals
        for i in range(1, len(intervals)):
            # If the earliest ending meeting is done before the next meeting starts
            if min_heap[0] <= intervals[i][0]:
                heappop(min_heap)  # Free up the room

            # Add the current meeting's end time to the heap
            heappush(min_heap, intervals[i][1])

        # The size of the heap represents the minimum number of meeting rooms required
        return len(min_heap)


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meeting_rooms =[]
        intervals.sort()
        meeting_rooms.append(intervals[0][1])

        for start,end in intervals[1:]:
            if meeting_rooms[0] > start:
                heapq.heappush(meeting_rooms,end)
            else:
                heapq.heappop(meeting_rooms)
                heapq.heappush(meeting_rooms,end)
        return len(meeting_rooms)

    def minMeetingRooms_2(self, intervals: List[List[int]]) -> int:
        meeting_rooms = []
        intervals.sort()
        meeting_rooms.append(intervals[0][1])

        for start, end in intervals[1:]:
            if meeting_rooms[0] <= start:
                heapq.heappop(meeting_rooms)
            heapq.heappush(meeting_rooms, end)
        return len(meeting_rooms)

