class Solution:
    def findCelebrity(self, n: int) -> int:
        # Step 1: Find a candidate in O(N)
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                # If candidate knows i, 'candidate' is not the celebrity.
                # 'i' becomes the new potential candidate.
                candidate = i

        # Step 2: Verify the candidate in O(N)
        # We must check if the candidate knows NO ONE and EVERYONE knows them.
        for i in range(n):
            if i == candidate:
                continue
            # If candidate knows i OR i doesn't know candidate, candidate is a fraud.
            if knows(candidate, i) or not knows(i, candidate):
                return -1

        return candidate




class Solution_Better_Bruteforce:
    def findCelebrity(self, n: int) -> int:
        for node in range(n):
            knows_nobody = True
            known_by_everyone = True

            for neighbour in range(n):
                if neighbour == node:
                    continue

                if knows(node, neighbour):   # node knows someone
                    knows_nobody = False
                    break

            if not knows_nobody:
                continue

            for neighbour in range(n):
                if neighbour == node:
                    continue

                if not knows(neighbour, node):   # someone doesn't know node
                    known_by_everyone = False
                    break

            if known_by_everyone:
                return node

        return -1


# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution_Naive_Bruteforce:
    def findCelebrity(self, n: int) -> int:
        '''
            Input: graph = [[1,1,0],
                [0,1,0],
                [1,1,1]]
        if I have incoming edges is n-1, outgoing edgesw is 0, then it is celebrity
        '''

        for node in range(n):
            incoming_edges = 0
            outgoing_edges = 0
            for neighbour in range(n):
                if neighbour == node:
                    continue
                if knows(node, neighbour):
                    outgoing_edges += 1
                if knows(neighbour, node):
                    incoming_edges += 1
            if outgoing_edges == 0 and incoming_edges == n - 1:
                return node

        return -1

