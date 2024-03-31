from typing import List
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meeting_rooms =[]
        intervals.sort()
        meeting_rooms.append(intervals[0][1])

        for i in range(1,len(intervals)):
            if meeting_rooms[0] > intervals[i][0]:
                meeting_rooms.append(intervals[i][1])
            else:
                meeting_rooms.pop(0)
                meeting_rooms.append(intervals[i][1])
            heapq.heapify(meeting_rooms)

        return len(meeting_rooms)

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meeting_rooms = []
        intervals.sort()
        meeting_rooms.append(intervals[0][1])

        for start, end in intervals[1:]:
            if meeting_rooms[0] > start:
                meeting_rooms.append(end)
            else:
                meeting_rooms.pop(0)
                meeting_rooms.append(end)
            heapq.heapify(meeting_rooms)

        return len(meeting_rooms)

    def minMeetingRooms_walkcc(self, intervals: List[List[int]]) -> int:
        meeting_rooms = []  # Store the end times of each room.

        for start, end in sorted(intervals):

            if meeting_rooms and  meeting_rooms[0] > start:
                meeting_rooms.append(end)
            else:
                meeting_rooms.pop(0)
                meeting_rooms.append(end)
            heapq.heapify(meeting_rooms)

        return len(meeting_rooms)