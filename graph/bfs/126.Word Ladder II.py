from collections import deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        queue = deque()
        queue.append((beginWord, 1, [beginWord]))
        if beginWord in word_set:
            word_set.remove(beginWord)

        result = []
        visited_this_level = set()
        min_level = float('inf')

        while queue:
            level_size = len(queue)
            local_visited = set()

            for _ in range(level_size):
                current_word, current_seq, current_list = queue.popleft()

                if current_word == endWord:
                    if current_seq <= min_level:
                        min_level = current_seq
                        result.append(current_list)
                    continue  # still allow other paths of same min length

                for i, ch in enumerate(current_word):
                    prefix_word = current_word[:i]
                    suffix_word = current_word[i + 1:]
                    for l in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = prefix_word + l + suffix_word
                        if new_word in word_set:
                            new_path = list(current_list)  # copy to avoid mutation
                            new_path.append(new_word)
                            queue.append((new_word, current_seq + 1, new_path))
                            local_visited.add(new_word)

            word_set -= local_visited  # remove only after whole level processed

        return result
from collections import deque, defaultdict
from typing import List

class Solution_with_Backtrack:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        queue = deque([beginWord])
        parents = defaultdict(set)  # child -> set of parents
        visited = set()
        found = False

        while queue and not found:
            level_visited = set()
            for _ in range(len(queue)):
                current_word = queue.popleft()

                for i in range(len(current_word)):
                    prefix = current_word[:i]
                    suffix = current_word[i+1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = prefix + c + suffix
                        if new_word in word_set:
                            if new_word == endWord:
                                found = True
                            if new_word not in visited:
                                queue.append(new_word)
                                level_visited.add(new_word)
                            parents[new_word].add(current_word)
            visited |= level_visited
            word_set -= level_visited  # Remove only after level ends

        # No path found
        if not found:
            return []

        # Backtrack paths from endWord to beginWord
        res = []

        def backtrack(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for parent in parents[word]:
                backtrack(parent, path + [parent])

        backtrack(endWord, [endWord])
        return res
