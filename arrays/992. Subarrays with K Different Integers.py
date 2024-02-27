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


