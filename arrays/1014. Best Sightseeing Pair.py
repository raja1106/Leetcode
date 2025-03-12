class Solution_Bruteforce:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = -1

        for i in range(len(values)):
            pair1 = values[i]

            for j in range(i + 1, len(values)):
                local_score = pair1 + values[j] + i - j
                max_score = max(max_score, local_score)

        return max_score


class Solution_Optimized:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # [2,1,5,3,3,4,6]  5+2 6 -i  --> 5+6+i-j (k,p) --> k-p+values[i]+p-i
        current_max = (values[0], 0)
        max_val = 0
        for i in range(1, len(values)):
            local_max = current_max[0] - current_max[1] + values[i] + current_max[1] - i # local_max = current_max[0]+ values[i]- i
            max_val = max(max_val, local_max)
            if current_max[0] < (values[i] + i):
                current_max = (values[i] + i, i)
        return max_val



