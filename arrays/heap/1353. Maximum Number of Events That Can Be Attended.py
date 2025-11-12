from collections import defaultdict
from heapq import heappush, heappop
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Greedy + Min Heap approach:
        Always attend the event that ends earliest among available ones.
        """

        # Group events by their start day for quick access
        events_starting_on_day = defaultdict(list)

        earliest_start_day = float('inf')
        latest_end_day = 0

        # Preprocess all events to find the global day range
        for start_day, end_day in events:
            events_starting_on_day[start_day].append(end_day)
            earliest_start_day = min(earliest_start_day, start_day)
            latest_end_day = max(latest_end_day, end_day)

        # Min-heap to store end days of events that are currently available
        active_event_end_days = []
        total_events_attended = 0

        # Iterate day by day from the earliest start to the latest end
        for current_day in range(earliest_start_day, latest_end_day + 1):

            # Remove expired events whose end day has already passed
            while active_event_end_days and active_event_end_days[0] < current_day:
                heappop(active_event_end_days)

            # Add all new events that start today
            for end_day in events_starting_on_day[current_day]:
                heappush(active_event_end_days, end_day)

            # Attend one event today — the one that ends earliest
            if active_event_end_days:
                heappop(active_event_end_days)
                total_events_attended += 1

        return total_events_attended


from typing import List
import heapq

class Solution_Another_heap:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort by start day
        events.sort(key=lambda e: e[0])
        n = len(events)

        end_heap: List[int] = []  # min-heap of end days
        i = 0                     # pointer over events
        day = 0
        attended = 0

        while i < n or end_heap:
            # If no active events, jump day to next start
            if not end_heap and i < n:
                day = max(day, events[i][0])

            # Add all events that start on/before 'day'
            while i < n and events[i][0] <= day:
                heapq.heappush(end_heap, events[i][1])
                i += 1

            # Remove expired events (end < current day)
            while end_heap and end_heap[0] < day:
                heapq.heappop(end_heap)

            # Attend one event today (the one that ends earliest)
            if end_heap:
                heapq.heappop(end_heap)
                attended += 1
                day += 1  # move to next day
            # else: heap empty; loop will jump to next event's start

        return attended

#Union Find

from typing import List
from collections import defaultdict

class Solution_Union_Find:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort by end day
        events.sort(key=lambda a: a[1])
        parent = {}  # DSU mapping: day -> next free day

        def find(x: int) -> int:
            # returns the smallest free day >= x
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        attended = 0
        for start, end in events:
            d = find(start)        # earliest free day >= start
            if d <= end:
                attended += 1
                parent[d] = find(d + 1)  # mark d taken; next free is find(d+1)

        return attended
