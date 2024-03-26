"""
A car travels from a starting position to a destination which is target miles east of the starting position.

There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.



Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
"""


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        current_fuel =startFuel
        count=0
        current_position=0
        for position,fuel in stations:
            if current_fuel > position:
                continue
            elif current_fuel < position:
                return -1
            else:
                current_position = position
                current_fuel = fuel
                if target == current_position:
                    return count
                else:
                    count += 1

    def minRefuelStops_Monst(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # Max-heap to store available fuel at stations we have passed
        fuel_maxheap = []
        # The position of the last station we processed
        previous_station_position = 0
        # The number of refueling stops we have made
        refuel_stops = 0
        # Add the target as a station to make sure we process the journey's end
        stations.append([target, 0])
        # Process each station on the route
        for position, fuel in stations:
            # Distance to the next station (or target)
            distance = position - previous_station_position
            startFuel -= distance  # Subtract the distance from the current fuel

            # Check if we need to refuel from passed stations (must take fuel from the station with the most fuel)
            while startFuel < 0 and fuel_maxheap:
                startFuel += -heappop(fuel_maxheap)  # Get fuel from the heap (invert the negative value)
                refuel_stops += 1  # Increment the refuel counter

            # If we cannot reach the next station/target and there is no more fuel in the heap, return -1
            if startFuel < 0:
                return -1

            # If the station offers fuel, add it to the heap (store as negative for max-heap)
            heappush(fuel_maxheap, -fuel)

            # Update the previous station position
            previous_station_position = position

        # Return the number of refueling stops after processing all stations
        return refuel_stops
























