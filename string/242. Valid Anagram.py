from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = [0] * 26
        t_count = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')
            s_count[idx] += 1
        for ch in t:
            idx = ord(ch) - ord('a')
            t_count[idx] += 1

        return tuple(s_count) == tuple(t_count)

class Solution_Efficient:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for ch in t:
            idx = ord(ch) - ord('a')
            count[idx] -= 1
            if count[idx] < 0:   # early exit if t has extra of some char
                return False

        return True
    
class Solution_using_Counter:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        return s_counter == t_counter