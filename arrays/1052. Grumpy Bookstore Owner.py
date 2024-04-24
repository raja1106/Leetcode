from typing import List


class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        k = minutes
        current_unsatisfied = 0
        for i in range(k):
            if grumpy[i] == 1:
                current_unsatisfied += customers[i]
        max_unsatisfied = current_unsatisfied
        for i in range(k, len(customers)):
            if grumpy[i] == 1:
                current_unsatisfied += customers[i]
            if grumpy[i - k] == 1:
                current_unsatisfied -= customers[i - k]
            max_unsatisfied = max(max_unsatisfied, current_unsatisfied)

        satisfied_customers = 0
        for j in range(len(customers)):
            if grumpy[j] == 0:
                satisfied_customers += customers[j]

        return satisfied_customers + max_unsatisfied
    def maxSatisfied_mysolution(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #findout in which window max grumy people
        k=minutes
        windowstart=0
        windowend=k-1
        max_grumpy=0
        local_grumpy=0
        for i in range(k):
            if grumpy[i] == 1:
                local_grumpy += customers[i]
        max_grumpy = local_grumpy
        for i in range(k,len(customers)):
            if grumpy[i] == 1:
                local_grumpy += customers[i]
            if grumpy[i-k] == 1:
                local_grumpy -= customers[i-k]
            if local_grumpy>max_grumpy:
                windowstart = i-k+1
                windowend=i
                max_grumpy = local_grumpy

        maxSatisfied=0

        for j in range(windowstart):
            if grumpy[j] == 0:
                maxSatisfied += customers[j]
        for j in range(windowend+1,len(customers)):
            if grumpy[j] == 0:
                maxSatisfied += customers[j]
        for j in range(windowstart,windowend+1):
            maxSatisfied += customers[j]

        return maxSatisfied