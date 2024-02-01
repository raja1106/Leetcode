from typing import List


# Input: row = [0,2,1,3]
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2 #TODO understand diff between / and //
        hmap = {}
        numOfSwaps = 0
        for i in range(len(row)):
            hmap[row[i]] = i

        for sofa in range(n):
            p1 = row[2 * sofa]
            if p1 % 2 == 0:
                p2Expected = p1 + 1
            else:
                p2Expected = p1 - 1
            while row[2 * sofa + 1] != p2Expected:
                if row[2 * sofa + 1] % 2 == 0:
                    partner = row[2 * sofa + 1] + 1
                else:
                    partner = row[2 * sofa + 1] - 1
                partnerIdx = hmap[partner]

                if partnerIdx % 2 == 0:
                    destinationIdx = partnerIdx + 1
                else:
                    destinationIdx = partnerIdx - 1
                hmap[row[2 * sofa + 1]] = destinationIdx
                hmap[row[destinationIdx]] = 2 * sofa + 1
                row[destinationIdx], row[2 * sofa + 1] = row[2 * sofa + 1], row[destinationIdx]

                numOfSwaps += 1

        return numOfSwaps