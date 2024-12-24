class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()  # Tracks visited rooms

        def explore_room(current_room):
            # Mark the current room as visited
            visited.add(current_room)

            # Explore all rooms accessible with the current room's keys
            for next_room in rooms[current_room]:
                if next_room not in visited:
                    explore_room(next_room)

        # Start the DFS exploration from room 0
        explore_room(0)

        # Check if all rooms were visited
        return len(visited) == len(rooms)




class Solution_Using_Stack:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()  # Tracks visited rooms
        stack = [0]  # Start DFS from room 0

        # Perform iterative DFS using a stack
        while stack:
            current_room = stack.pop()
            if current_room not in visited:
                # Mark the room as visited
                visited.add(current_room)

                # Add all unvisited neighboring rooms to the stack
                for next_room in rooms[current_room]:
                    if next_room not in visited:
                        stack.append(next_room)

        # Check if all rooms were visited
        return len(visited) == len(rooms)


from typing import List
from collections import deque


class Solution_Using_BFS:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()  # Tracks visited rooms
        queue = deque([0])  # Start BFS from room 0

        # Perform BFS using a queue
        while queue:
            current_room = queue.popleft()
            if current_room not in visited:
                # Mark the room as visited
                visited.add(current_room)

                # Add all unvisited neighboring rooms to the queue
                for next_room in rooms[current_room]:
                    if next_room not in visited:
                        queue.append(next_room)

        # Check if all rooms were visited
        return len(visited) == len(rooms)
