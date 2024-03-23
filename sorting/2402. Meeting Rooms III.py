"""
You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.



Example 1:

Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0
Explanation:
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0.
Example 2:

Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: 1
Explanation:
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1.
"""
from typing import List
from heapq import heapify,heappop,heappush
from collections import Counter
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms_available = []
        for i in range(n):
            rooms_available.append([0, i])

        heapify(rooms_available)
        map = Counter()
        meetings.sort(key=lambda x: x[0])

        for i in range(len(meetings)):
            earliest_available_rooms =[]
            while rooms_available and rooms_available[0] <= meetings[0]:
                room =heappop(rooms_available)
                earliest_available_rooms.append([room[1],room[0]])

            earliest_available_room = heappop(rooms_available)
            map[earliest_available_room[1]] += 1
            earliest_available_room[0] = max(earliest_available_room[0], meetings[i][0]) + (
                        meetings[i][1] - meetings[i][0])
            heappush(rooms_available, earliest_available_room)

        room_list = map.most_common()
        print(type(room_list))
        return room_list[0][0]

    def mostBookedMonster(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()

        busy_rooms_heap = []
        idle_rooms_heap = list(range(n))
        heapify(idle_rooms_heap)
        count = [0] * n
        #meeting_count = Counter()

        for start_time,end_time in meetings:
            while busy_rooms_heap and busy_rooms_heap[0][0] <= start_time:
                room_index = heappop(busy_rooms_heap)[1]
                heappush(idle_rooms_heap,room_index)

            if idle_rooms_heap:
                room_index = heappop(idle_rooms_heap)
                count[room_index] += 1
                heappush(busy_rooms_heap,[end_time,room_index])
            else:  # No idle rooms; wait for the first available room
                earliest_end, room_index = heappop(busy_rooms_heap)
                count[room_index] += 1
                heappush(busy_rooms_heap, [earliest_end + end_time - start_time, room_index])

        #room_list = meeting_count.most_common()
        #return room_list[0][0]
        return count.index(max(count))




























