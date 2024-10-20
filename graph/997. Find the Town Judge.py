class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < N - 1:
            return -1

        in_degree = [0] * (N + 1)
        out_degree = [0] * (N + 1)

        for a, b in trust:
            out_degree[a] += 1
            in_degree[b] += 1

        for i in range(1, N + 1):
            if in_degree[i] == N - 1 and out_degree[i] == 0:
                return i
        return -1