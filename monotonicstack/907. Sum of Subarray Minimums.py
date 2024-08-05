class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        local_ans = [0] * len(arr)
        stack = []
        global_count = 0

        for i in range(len(arr)):
            while stack and stack[-1][0] >= arr[i]:
                stack.pop()
            if stack:
                span = i - stack[-1][1]
                local_ans[i] = span * arr[i] + local_ans[stack[-1][1]]
            else:
                span = i+1
                local_ans[i] = span * arr[i]
            global_count = (global_count + local_ans[i]) % MOD
            stack.append((arr[i],i))
        return global_count


