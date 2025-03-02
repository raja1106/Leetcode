from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[:k])
        required_sum = k*threshold
        valid_subarray_count=0
        if window_sum >= required_sum:
            valid_subarray_count+=1

        for i in range(k,len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i-k]
            if window_sum >= required_sum:
                valid_subarray_count += 1
        return valid_subarray_count

