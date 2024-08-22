from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            current_word, level = queue.popleft()

            for i in range(len(current_word)):
                # Try changing each letter in the current word
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = current_word[:i] + c + current_word[i + 1:]

                    # If we find the endWord, return the current level + 1
                    if new_word == endWord:
                        return level + 1

                    # If new_word is in word_set, add it to the queue and remove from the set
                    if new_word in word_set:
                        word_set.remove(new_word)
                        queue.append((new_word, level + 1))

        return 0
