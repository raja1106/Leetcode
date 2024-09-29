from collections import deque, defaultdict
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Create a mapping from each bus stop to the buses that stop there
        stop_to_buses = defaultdict(list)
        for bus_index in range(len(routes)):
            for stop in routes[bus_index]:
                stop_to_buses[stop].append(bus_index)

        # Initialize the queue for BFS and a set to track visited buses
        queue = deque()
        visited_buses = set()

        # Enqueue all stops accessible by buses from the source stop
        for bus_index in stop_to_buses[source]:
            visited_buses.add(bus_index)
            for stop in routes[bus_index]:
                queue.append((stop, 1))

        # Perform BFS to find the shortest path to the target stop
        while queue:
            current_stop, buses_taken = queue.popleft()

            if current_stop == target:
                return buses_taken

            for bus_index in stop_to_buses[current_stop]:
                if bus_index not in visited_buses:
                    visited_buses.add(bus_index)
                    for stop in routes[bus_index]:
                        queue.append((stop, buses_taken + 1))

        return -1
