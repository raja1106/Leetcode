class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        pattern_freq = Counter(s1)

        window_freq = Counter(s2[:k])

        if window_freq == pattern_freq:
            return True

        for i in range(k, len(s2)):
            window_freq[s2[i]] += 1
            window_freq[s2[i - k]] -= 1
            if window_freq[s2[i - k]] == 0:
                del window_freq[s2[i - k]]
            if window_freq == pattern_freq:
                return True

        return False




