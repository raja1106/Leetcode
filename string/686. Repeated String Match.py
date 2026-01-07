class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        orinial_a = a
        b_len = len(b)
        count = 1

        while len(a) < b_len:
            a = a + orinial_a
            count += 1

        if a.find(b) != -1:
            return count

        count += 1
        a = a + orinial_a

        if a.find(b) != -1:
            return count
        else:
            return -1

class Solution_better_bruteforce:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(a), len(b)

        # Minimum repeats so that repeated a length >= b length
        k = (m + n - 1) // n

        s = a * k
        if b in s:
            return k

        s = a * (k + 1)
        if b in s:
            return k + 1

        return -1
