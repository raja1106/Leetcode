class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 0
        end = n
        while start <= end:
            mid = start + (end-start)//2
            x = mid*(mid+1)//2
            if x == n:
                return mid
            elif x < n:
                start = mid+1
            else:
                end = mid-1
        return end


class Solution_With_Two_Split:
    def arrangeCoins(self, n: int) -> int:
        # Initialize the search range
        start = 0  # Minimum possible number of rows
        end = n  # Maximum possible number of rows

        # Perform binary search to find the maximum full rows
        while start <= end:
            # Calculate the middle point of the current search range
            mid = start + (end - start) // 2

            # Calculate the total number of coins required to fill 'mid' rows
            # This is derived from the formula: sum of first 'mid' natural numbers
            x = mid * (mid + 1) // 2

            # If the total coins used is less than or equal to 'n',
            # it means we can potentially fill more rows
            if x <= n:
                start = mid + 1  # Try to fit more rows
            else:
                # If the total exceeds 'n', reduce the search space
                end = mid - 1  # Fewer rows can be formed

        # Return the last valid number of rows (stored in 'end')
        return end


