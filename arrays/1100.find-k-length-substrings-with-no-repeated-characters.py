class Solution:
    #initialization
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        window_map={}
        result=0
        for i in range(k):
            if s[i] in window_map:
                window_map[s[i]] +=1
            else:
                window_map[s[i]] =1
        valid_window=True
        for value in window_map.values():
            if value > 1:
                valid_window=False
        if valid_window  == True:
            result=1

        for i in range(k,len(s)):
            if s[i] in window_map:
                window_map[s[i]] +=1
            else:
                window_map[s[i]] =1
            if s[i-k] in window_map:
                window_map[s[i-k]] -= 1

            valid_window = True
            for value in window_map.values():
                if value > 1:
                    valid_window = False
            if valid_window == True:
                result += 1

        return result
