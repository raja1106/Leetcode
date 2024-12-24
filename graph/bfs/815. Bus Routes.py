from collections import deque, defaultdict
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Create a mapping from each bus stop to the buses that stop there
        stop_to_buses_map = defaultdict(list)
        for bus_index in range(len(routes)):
            for stop in routes[bus_index]:
                stop_to_buses_map[stop].append(bus_index)

        # Initialize the queue for BFS and a set to track visited buses
        queue = deque()
        visited_buses = set()

        # Enqueue all stops accessible by buses from the source stop
        for bus_index in stop_to_buses_map[source]:
            visited_buses.add(bus_index)
            for stop in routes[bus_index]:
                queue.append((stop, 1))

        # Perform BFS to find the shortest path to the target stop
        while queue:
            current_stop, buses_taken = queue.popleft()

            if current_stop == target:
                return buses_taken

            for bus_index in stop_to_buses_map[current_stop]:
                if bus_index not in visited_buses:
                    visited_buses.add(bus_index)
                    for stop in routes[bus_index]:
                        queue.append((stop, buses_taken + 1))

        return -1




class Solution_Another_Way:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # If the source and target are the same, no bus needs to be taken.
        if source == target:
            return 0

        # Convert each route to a set for faster checks later on.
        sets_of_routes = [set(route) for route in routes]

        # Create a dictionary where each stop maps to a list of buses (routes) that visit that stop.
        stop_to_buses_dict = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses_dict[stop].append(i)

        # Build a graph where each node represents a bus and edges connect buses that share a common stop.
        bus_graph = defaultdict(list)
        for buses in stop_to_buses_dict.values():
            num_buses = len(buses)
            for i in range(num_buses):
                for j in range(i + 1, num_buses):
                    first, second = buses[i], buses[j]
                    bus_graph[first].append(second)
                    bus_graph[second].append(first)

        # Start BFS from the buses that can be taken from the source stop.
        queue = deque(stop_to_buses_dict[source])
        number_of_buses = 1
        visited_buses = set(stop_to_buses_dict[source])

        while queue:
            # Process all nodes on the current level.
            for _ in range(len(queue)):
                current_bus = queue.popleft()

                # If the target stop is in the current bus's route, return the number of buses needed.
                if target in sets_of_routes[current_bus]:
                    return number_of_buses

                # Check unvisited buses that can be reached from the current bus.
                for adjacent_bus in bus_graph[current_bus]:
                    if adjacent_bus not in visited_buses:
                        visited_buses.add(adjacent_bus)
                        queue.append(adjacent_bus)

            # Increment the number of buses needed as we are now moving to the next level in BFS.
            number_of_buses += 1

        # If no path is found, return -1 to signify that destination cannot be reached.
        return -1
