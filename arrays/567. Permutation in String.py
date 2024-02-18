class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = {}
        map2={}
        k=len(s1)
        if len(s2)<k:
            return False
        for i in range(k):
            if s1[i] in map1:
                map1[s1[i]] +=1
            else:
                map1[s1[i]] = 1

        for j in range(k):
            if s2[j] in map2:
                map2[s2[j]] +=1
            else:
                map2[s2[j]] = 1

        if (map1 == map2):
            return True

        for j in range(k,len(s2)):
            if s2[j] in map2:
                map2[s2[j]] +=1
            else:
                map2[s2[j]] = 1

            map2[s2[j-k]] -=1
            if map2[s2[j-k]] == 0:
                map2.pop(s2[j-k])
            if (map1 == map2):
                return True

        return False
