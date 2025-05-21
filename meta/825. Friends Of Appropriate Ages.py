from typing import List
from collections import Counter


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # Count the frequency of each age
        age_count = Counter(ages)
        total_requests = 0

        # Iterate through all possible ages for x and y
        for age_x in age_count:
            for age_y in age_count:
                if age_y <= 0.5 * age_x + 7:
                    continue
                if age_y > age_x:
                    continue
                if age_y > 100 and age_x < 100:
                    continue

                # If the ages are valid, calculate the number of requests
                if age_x == age_y:
                    total_requests += age_count[age_x] * (age_count[age_y] - 1)
                else:
                    total_requests += age_count[age_x] * age_count[age_y]

        return total_requests


class Solution_Binary_Search:
    def numFriendRequests(self, ages: List[int]) -> int:
        bucket = [0] * 121
        for age in ages:
            bucket[age] += 1

        prefix = [0] * 121
        for i in range(1, 121):
            prefix[i] = prefix[i - 1] + bucket[i]

        res = 0
        for age in range(15, 121):  # no one <15 can send requests
            if bucket[age] == 0:
                continue
            min_age = int(age / 2 + 7)
            count = prefix[age] - prefix[min_age]
            res += bucket[age] * (count - 1)  # subtract self

        return res

