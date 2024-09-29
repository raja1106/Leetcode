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
