from typing import List


class Solution:
    """
    Initial Values for Binary Search:

The initial value of start should be the maximum weight in the weights array, as the minimum possible capacity must be at least as large as the heaviest item.
The initial value of end should be the sum of all weights, as the maximum possible capacity is when the ship carries all items in one trip.
    """
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)

        def get_days(ship_capacity):
            day_count = 1
            load = 0
            for i in range(len(weights)):
                load += weights[i]
                if load > ship_capacity:
                    day_count += 1
                    load = weights[i]
            return day_count

        while start <= end:
            mid = start + (end - start) // 2
            days_needed = get_days(mid)

            if days_needed > days:
                start = mid + 1
            else:
                end = mid - 1

        return start


    """
    
    different ways of implementing it
        def get_days(ship_capacity):
            days_for_current_capacity = 1
            capacity = ship_capacity
            for i in range(len(weights)):
                if capacity >= weights[i]:
                    capacity -= weights[i]
                else:
                    days_for_current_capacity += 1
                    capacity = ship_capacity
                    capacity -= weights[i]
            return days_for_current_capacity
    """
