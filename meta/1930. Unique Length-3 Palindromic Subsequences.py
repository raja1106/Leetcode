class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        for ch in set(s):  # Loop through unique characters (max 26 lowercase)
            first = s.find(ch)
            last = s.rfind(ch)
            if last - first >= 2:
                mid_chars = set(s[first + 1:last])
                result += len(mid_chars)
        return result


class Solution_Bruteforce_Way:
    def countPalindromicSubsequence(self, s: str) -> int:
        total_count = 0
        result_set = set()
        memo = set()
        def is_palindrom(list_s):
            if list_s[2] == list_s[0]:
                return True
            else:
                return False
        def dfs(i,slate):
            if (i,tuple(slate)) in memo:
                return
            #nonlocal total_count
            if i == len(s) or len(slate) == 3:
                if len(slate) == 3 and is_palindrom(slate):
                    result_set.add(''.join(slate))
                return
            #exclude
            dfs(i+1,slate)
            #include
            slate.append(s[i])
            dfs(i+1,slate)
            slate.pop()
            memo.add((i,tuple(slate)))
        dfs(0,[])
        return len(result_set)
        #aabca

