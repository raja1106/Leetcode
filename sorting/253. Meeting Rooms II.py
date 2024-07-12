from typing import List
import heapq
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

