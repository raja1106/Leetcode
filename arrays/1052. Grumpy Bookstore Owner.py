from typing import List


class Solution:

    def maxSatisfied_Algomonster(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        unsatisfied = sum(customer * grumpiness for customer, grumpiness in zip(customers, grumpy))
        total_customers = sum(customers)
        temp_improved = max_improved = 0
        for minute_index, (customer, grumpiness) in enumerate(zip(customers, grumpy), 1):
            temp_improved += customer * grumpiness
            if (start_index := minute_index - minutes) >= 0:
                max_improved = max(max_improved, total_customers - (unsatisfied - temp_improved))
                temp_improved -= customers[start_index] * grumpy[start_index]
        return max_improved
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