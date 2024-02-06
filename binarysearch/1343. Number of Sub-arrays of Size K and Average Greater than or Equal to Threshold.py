from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_sum = sum(arr[:k])
        threshold_sum=k*threshold
        total=0
        if current_sum >= threshold_sum:
            total+=1

        for i in range(k,len(arr)):
            current_sum +=arr[i]-arr[i-k]
            if current_sum >= threshold_sum:
                total += 1
        return total

