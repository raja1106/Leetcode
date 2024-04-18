class Solution: #Not Working
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        global_count=0
        leftge,leftel =0,0
        hmapge, hmapel = {}, {}

        for i in range (len(nums)):
            if nums[i] in hmapel:
                hmapel[nums[i]] += 1
            else:
                hmapel[nums[i]] = 1

            if nums[i] in hmapge:
                hmapel[nums[i]] += 1
            else:
                hmapge[nums[i]] = 1

            while leftel <=i and len(hmapel) >=k:
                hmapel[nums[leftel]] -= 1

                if hmapel[nums[leftel]] == 0:
                    del hmapel[nums[leftel]]
                leftel += 1

            while leftge <=i and len(hmapge) >k:
                hmapge[nums[leftel]] -= 1

                if hmapge[nums[leftel]] == 0:
                    del hmapge[nums[leftel]]
                leftge += 1
            global_count += leftel-leftge

        return  global_count

    def subarraysWithKDistinctRecursion(self, nums: List[int], k: int) -> int: #Working with Time limit exceeded
        return self.helper(nums, k, 0, {})

    def helper(self, nums: List[int], k: int, index: int, counter):
        if (index == len(nums)):
            return 0
        self.addElement(counter, nums[index])
        result = 0
        if len(counter) == k:
            result += 1
        if len(counter) > k:
            self.removeElement(counter, nums[index])
            return result
        result += self.helper(nums, k, index + 1, counter)
        self.removeElement(counter, nums[index])
        if (len(counter) == 0):
            result += self.helper(nums, k, index + 1, counter)
        return result

    def addElement(self, counter, element):
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1

    def removeElement(self, counter, element):
        if counter[element] == 1:
            del counter[element]
        else:
            counter[element] -= 1


