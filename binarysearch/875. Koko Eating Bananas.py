import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        startk=1
        endk=max(piles)

        while startk <= endk:
            mid = startk + (endk-startk)//2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/mid)
            # hours = sum(math.ceil(pile / mid) for pile in piles) Other way of calculation
            if hours <= h:
                endk = mid-1
            else:
                startk = mid+1
        return startk
