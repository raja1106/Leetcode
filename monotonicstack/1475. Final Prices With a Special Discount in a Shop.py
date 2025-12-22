from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        [8,4,6,2,3]

        """
        st = []  # looking for previous smallest or equal element
        result = [price for price in prices]
        for i in range(len(prices) - 1, -1, -1):
            while st and st[-1] > prices[i]:
                st.pop()

            if st:
                result[i] = prices[i] - st[-1]

            st.append(prices[i])

        return result

class Solution_BruteForce:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        [8,4,6,2,3]

        """

        result = [price for price in prices]

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    result[i] = prices[i]-prices[j]
                    break

        return result