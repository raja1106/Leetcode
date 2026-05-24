
from typing import List

class Solution_OnePassBest:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position and speed
        cars = [(pos, spd) for pos, spd in zip(position, speed)]

        # Sort cars by position in descending order (closest to target first)
        cars.sort(reverse=True)

        fleet_times = []  # Stack to store times of fleet leaders

        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            fleet_times.append(time_to_target)

            # If a car catches up to or arrives earlier than the previous fleet,
            # they merge — remove the current one (same fleet)
            if len(fleet_times) >= 2 and fleet_times[-1] <= fleet_times[-2]:
                fleet_times.pop()

        return len(fleet_times)

class Solution_Two_Pass:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = []

        for p, s in zip(position, speed):
            paired.append((p, s))

        paired.sort()

        time = []

        for pair in paired:
            time_taken = (target - pair[0]) / pair[1]

            time.append(time_taken)
        count = 1
        last_reached_time = time[-1]
        for i in range(len(time) - 2, -1, -1):
            current_time = time[i]

            if current_time > last_reached_time:
                count += 1
                last_reached_time = current_time

        return count
