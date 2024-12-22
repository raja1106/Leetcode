from typing import List


class Solution:
    """
    Initial Values for Binary Search:

The initial value of start should be the maximum weight in the weights array, as the minimum possible capacity must be at least as large as the heaviest item.
The initial value of end should be the sum of all weights, as the maximum possible capacity is when the ship carries all items in one trip.

        weights = [1,2,3,4,5,6,7,8,9,10]

        left region denotes --> by these ship_capacity values in left region, you can't ship all items within num_of_days("days" in input)
        right region denotes --> by these ship_capacity values in right region, you can ship all items within num_of_days("days" in input).. since question is min_val
        from the right region, we are returning "R", and that is "start"

        llllllllllRrrrrrrrrr
        'R' --> this 'R' we are trying to find. 'R' which is "starting of the right region". As any Binary Search Problem,
        here we are moving "start" pointer to "right region" and moving "end" pointer to "left region".
        After every iteration in while loop, we are reducing search region by n/2. so T(n) is log(n)

        if can_load(k) returns True (that is days_needed <= days): end = mid-1
            return False (that is days_needed > days) --> start = mid+1
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
class Solution_Another_Approach:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Finds the minimum ship capacity required to ship all packages within the given number of days.

        Args:
            weights (List[int]): Array of package weights.
            days (int): Number of days within which packages must be shipped.

        Returns:
            int: Minimum ship capacity.
        """
        start, end = max(weights), sum(weights)

        def can_ship(capacity: int) -> bool:
            """
            Determines if all packages can be shipped within the given days using the specified capacity.

            Args:
                capacity (int): The ship's capacity to test.

            Returns:
                bool: True if the capacity is sufficient, False otherwise.
            """
            num_days, current_capacity = 1, 0

            for weight in weights:
                if current_capacity + weight > capacity:
                    num_days += 1
                    current_capacity = 0
                current_capacity += weight

                if num_days > days:  # Early exit
                    return False

            return True

        # Perform binary search to find the minimum feasible capacity
        while start <= end:
            mid = (start + end) >> 1
            if can_ship(mid):
                end = mid - 1  # Try for a smaller capacity
            else:
                start = mid + 1  # Increase capacity

        return start
