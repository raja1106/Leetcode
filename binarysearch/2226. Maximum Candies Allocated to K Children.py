class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        '''

        1 to max(candies)

        lllllllLRrrrrrrr

        left region --> possible ranges
        right_range. --> not possible ranges

        L is the max possible range, return 'end'

        '''

        def can_allocate(num_candies):  # 8
            count = 0

            for candie in candies:
                count_by_candie = candie // num_candies
                count += count_by_candie

            return count >= k

        start = 1  # 6
        end = max(candies)  # 5

        while start <= end:
            mid = start + (end - start) // 2

            if can_allocate(mid):
                start = mid + 1
            else:
                end = mid - 1

        return end