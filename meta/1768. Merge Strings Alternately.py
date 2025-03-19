class Solution:
    def mergeAlternately(self, first_word: str, second_word: str) -> str:
        first_length = len(first_word)
        second_length = len(second_word)
        first_index = 0
        second_index = 0
        merged_result = []
        is_first_turn = True  # True means it's first_word's turn; False means second_word's turn

        while first_index < first_length and second_index < second_length:
            if is_first_turn:
                merged_result.append(first_word[first_index])
                first_index += 1
                is_first_turn = False
            else:
                merged_result.append(second_word[second_index])
                second_index += 1
                is_first_turn = True

        # Append any remaining characters from first_word or second_word
        if first_index < first_length:
            merged_result.extend(first_word[first_index:])
        if second_index < second_length:
            merged_result.extend(second_word[second_index:])

        return ''.join(merged_result)

class Solution3:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        words = []  # n words
        words.append(word1)
        words.append(word2)
        # Determine the maximum length among all strings
        max_length = max(len(word) for word in words)  # O(n)

        # Loop through each character position
        for i in range(max_length):  # O(m)
            for word in words:  # O(n)
                if i < len(word):
                    result.append(word[i])

        return "".join(result)  # O(m*n)