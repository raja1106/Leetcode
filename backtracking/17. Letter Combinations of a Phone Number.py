from typing import List

"""
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if digits:
            self.get_words_from_phone_number_util(digits, 0, [], result)
        return result

    def get_words_from_phone_number_util(self, digits: str, i: int, slate: List[str], result: List[str]) -> None:
        phone_dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        #Base case
        if i == len(digits):
            result.append(''.join(slate))
            return

        #Recursive case
        choices = phone_dict[digits[i]]

        for choice in choices:
            slate.append(choice)
            self.get_words_from_phone_number_util(digits, i + 1, slate, result)
            del slate[-1]





















