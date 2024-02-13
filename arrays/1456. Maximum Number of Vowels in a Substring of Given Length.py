class Solution:
    #Input: s = "abciiidef", k = 3

    def maxVowels(self, s: str, k: int) -> int:
        vowel_letters = {'a', 'e', 'i', 'o', 'u'}
        local_size = 0
        for i in range(k):
            if s[i] in vowel_letters:
                local_size += 1

        max_size =local_size

        for i in range(k,len(s)):
            if s[i] in vowel_letters:
                local_size += 1
            if s[i-k] in vowel_letters:
                local_size -= 1
            max_size = max(local_size,max_size)

        return max_size