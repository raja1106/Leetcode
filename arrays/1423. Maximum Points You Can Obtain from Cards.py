class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_size=len(cardPoints)-k
        min_sum=sum(cardPoints[:window_size])
        current_sum=min_sum

        for i in range(window_size,len(cardPoints)):
            current_sum += cardPoints[i]
            current_sum -= cardPoints[i-window_size]

            min_sum = min(current_sum,min_sum)

        return sum(cardPoints)-min_sum


