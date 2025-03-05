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


class Solution_BruteForce:
    def minSwapsCouples(self, row: List[int]) -> int:
        swap_count = 0

        def swap_positions(index1: int, index2: int) -> None:
            row[index1], row[index2] = row[index2], row[index1]

        # Iterate over the row two seats at a time (each pair is a couple)
        for i in range(0, len(row), 2):
            first_person = row[i]
            # Determine the expected partner: even-indexed person should have partner = first_person + 1,
            # odd-indexed person should have partner = first_person - 1.
            expected_partner = first_person + 1 if first_person % 2 == 0 else first_person - 1

            # If the expected partner is already next to the first person, no swap is needed.
            if row[i + 1] == expected_partner:
                continue

            # Otherwise, search for the expected partner in the rest of the row.
            for j in range(i + 2, len(row)):
                if row[j] == expected_partner:
                    swap_positions(j, i + 1)
                    swap_count += 1
                    break

        return swap_count
