from collections import defaultdict, Counter


def can_form_step_optimized(s1, s2):
    # s1 should be shorter by exactly one letter
    if len(s1) + 1 != len(s2):
        return False

    # Count frequencies of each character
    count1 = Counter(s1)
    count2 = Counter(s2)

    # Check if adding exactly one letter forms the longer word
    diff = 0
    for char in count2:
        if count2[char] > count1.get(char, 0):
            diff += count2[char] - count1.get(char, 0)
        if diff > 1:
            return False
    return diff == 1
def step_index_optimized(wordlist):
    index = defaultdict(list)
    words_by_length = defaultdict(list)

    # Group words by their length
    for word in wordlist:
        words_by_length[len(word)].append(word)

    # Compare words of length L with words of length L + 1
    for length in words_by_length:
        if length + 1 not in words_by_length:
            continue
        for w1 in words_by_length[length]:
            for w2 in words_by_length[length + 1]:
                if can_form_step_optimized(w1, w2):
                    index[w1].append(w2)
    return index
def getChilds(wordsList):
    results={}
    wordsDict = {}
    for i in range(len(wordsList)):
        # rearrage the word in alphabetical order
        word = ''.join(sorted(wordsList[i]))
        wordsDict[word]=i

    for word in wordsList:
        reWord = ''.join(sorted(word))
        # remove one char in the word and loop through
        for i in range(len(reWord)):
            newWord = reWord[:i]+reWord[i+1:]
            if newWord in wordsDict:
                if word not in results:
                    results[word]=[]
                results[word].apppend(wordsList[wordsDict[newWord]])
    return results

# Example usage
wordlist = [
    "OF", "FOR", "NO", "ON", "NOT", "FROM", "ONE", "INTO", "OUGHT", "THOUGH",
    "SOUGHT", "THOUGHT", "NOW", "FOUR", "FORM", "OFF", "POINT", "LEFT", "FORMS"
]
print(getChilds(wordsList))

one_letter_steps_index_optimized = step_index_optimized(wordlist)

# Pretty-print the result
for word, steps in one_letter_steps_index_optimized.items():
    print(f"{word}: {steps}")


def can_form_step(s1, s2):
    # s1 should be shorter by exactly one letter
    if len(s1) + 1 != len(s2):
        return False

    # Count frequencies of each character
    count1 = Counter(s1)
    count2 = Counter(s2)

    # Check if we can form s2 by adding exactly one letter to s1
    diff = 0
    for char in count2:
        if count2[char] > count1.get(char, 0):
            diff += count2[char] - count1.get(char, 0)
        if diff > 1:
            return False

    return diff == 1


def step_index(wordlist):
    index = defaultdict(list)

    for i, w1 in enumerate(wordlist):
        for w2 in wordlist:
            if can_form_step(w1, w2):
                index[w1].append(w2)

    return index


# Example usage
wordlist = [
    "OF", "FOR", "NO", "ON", "NOT", "FROM", "ONE", "INTO", "OUGHT", "THOUGH",
    "SOUGHT", "THOUGHT", "NOW", "FOUR", "FORM", "OFF", "POINT", "LEFT", "FORMS"
]

one_letter_steps_index = step_index(wordlist)

# Pretty-print the result
for word, steps in one_letter_steps_index.items():
    print(f"{word}: {steps}")
