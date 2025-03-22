class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        if not sentence:
            return ""

        result = []
        # Using sentence.split() to handle multiple spaces gracefully
        for i, word in enumerate(sentence.split()):
            if word[0].lower() in ('a', 'e', 'i', 'o', 'u'):
                modified_word = word + 'ma'
            else:
                modified_word = word[1:] + word[0] + 'ma'
            # Append the appropriate number of 'a's
            modified_word += 'a' * (i + 1)
            result.append(modified_word)

        return ' '.join(result)



parent = list(range(5))
print(parent)