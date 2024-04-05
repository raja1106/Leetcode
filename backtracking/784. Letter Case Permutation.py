from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        self.generatePermutations(0, list(s), [], result)
        return result

    def generatePermutations(self, i: int, s: List[str], slate: List[str], result:List[str]):
        if i == len(s):
            result.append(''.join(slate))
            return

        if s[i].isdigit():
            slate.append(s[i])
            self.generatePermutations(i + 1, s, slate, result)
            del slate[-1]
        else:
            slate.append(s[i].upper())
            self.generatePermutations(i + 1, s, slate, result)
            del slate[-1]
            slate.append(s[i].lower())
            self.generatePermutations(i + 1, s, slate, result)
            del slate[-1]
        return
