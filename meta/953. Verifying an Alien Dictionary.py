from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a mapping of each character to its rank according to the alien dictionary
        order_index = {char: i for i, char in enumerate(order)}

        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    break
        return True

class Solution_AnotherWay:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a mapping of each character to its rank according to the alien dictionary
        order_index = {char: i for i, char in enumerate(order)}

        # Function to convert a word into its corresponding rank list based on the alien order
        def transform(word):
            return [order_index[char] for char in word]

        # [0,6,1,1,14].
        # Iterate through the words and compare each word with the next one
        for i in range(len(words) - 1):
            # Compare the transformed versions of the words
            if transform(words[i]) > transform(words[i + 1]):
                return False

        # If all words are in order, return True
        return True
