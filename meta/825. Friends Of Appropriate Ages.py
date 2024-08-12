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
