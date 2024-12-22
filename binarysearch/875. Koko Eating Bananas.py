import math

"""
Determines the minimum eating speed required to eat all banana piles within the given hours.

        left region denotes --> by these speed values in left region, you can't eat all items within h hours
        right region denotes --> by these  speed values in right region, you can eat all items within h hours.. since question is min_val
        from the right region, we are returning "R", and that is "start"

        llllllllllRrrrrrrrrr
        
        'R' --> this 'R' we are trying to find. 'R' which is "starting of the right region". As any Binary Search Problem,
        here we are moving "start" pointer to "right region" and moving "end" pointer to "left region".
        After every iteration in while loop, we are reducing search region by n/2. so T(n) is log(n)


"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        startk = 1
        endk = max(piles)

        while startk <= endk:
            mid = startk + (endk - startk) // 2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)
            # hours = sum(math.ceil(pile / mid) for pile in piles) Other way of calculation
            if hours <= h:
                endk = mid - 1
            else:
                startk = mid + 1
        return startk


class Solution_Another_Approach:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Determines the minimum eating speed required to eat all banana piles within the given hours.

        start is min_speed
        end is max_speed here

        """
        min_speed, max_speed = 1, sum(piles)

        def can_finish_all(speed: int) -> bool:
            """
            Checks if all piles can be finished within h using the given speed.

            Args:
                speed (int): Eating speed to test.

            Returns:
                bool: True if the speed is sufficient, False otherwise.
            """
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / speed)
            return total_hours <= h

        # Perform binary search to find the minimum eating speed
        while min_speed <= max_speed:
            mid_speed = min_speed + (max_speed - min_speed) // 2
            if can_finish_all(mid_speed):
                max_speed = mid_speed - 1
            else:
                min_speed = mid_speed + 1

        return min_speed
