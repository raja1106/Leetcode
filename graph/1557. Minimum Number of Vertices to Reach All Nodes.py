class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        outgoing = [0] * n
        incoming = [0] * n

        for src, dst in edges:
            outgoing[src] += 1
            incoming[dst] += 1

        result = []
        for i in range(n):
            if incoming[i] == 0:
                result.append(i)

        return result
