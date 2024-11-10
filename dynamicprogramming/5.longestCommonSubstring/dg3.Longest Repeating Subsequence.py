class Solution:
  def findLRSLength(self,text):
    memo = {}

    def findLCSLengthRecursive(s1, s2, i1, i2):
        if i1 == len(s1) or i2 == len(s2):
            return 0

        # Memoization key
        if (i1, i2) in memo:
            return memo[(i1, i2)]

        # Case 1: Characters match and indices are not the same
        if s1[i1] == s2[i2] and i1 != i2:
            count1 = 1 + findLCSLengthRecursive(s1, s2, i1 + 1, i2 + 1)
        else:
            count1 = 0

        # Case 2: Skip one character in s1
        count2 = findLCSLengthRecursive(s1, s2, i1 + 1, i2)

        # Case 3: Skip one character in s2
        count3 = findLCSLengthRecursive(s1, s2, i1, i2 + 1)

        # Memoize the maximum value
        memo[(i1, i2)] = max(count1, count2, count3)
        return memo[(i1, i2)]

    # Call the recursive function with both strings set to `text`
    return findLCSLengthRecursive(text, text, 0, 0)
