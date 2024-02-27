class Solution:#Not Working
    def minWindow(self, s: str, t: str) -> str:
        left=0
        smap, tmap = {},{}
        min_length=len(s)+1
        start_index,end_index =0,0
        for i in range(len(t)):
            if t[i] in tmap:
                tmap[t[i]] += 1
            else:
                tmap[t[i]] = 1

        for i in range(len(s)):
            if s[i] in smap:
                smap[s[i]] += 1
            else:
                smap[s[i]] = 1

            while left <= i and len(smap)>len(tmap):
                smap[s[left]] -= 1
                if smap[s[left]] == 0:
                    del smap[s[left]]
                left += 1

            if smap == tmap:
                if (i-left+1) <min_length:
                    start_index =left
                    end_index=i
        return s[start_index:end_index+1]
