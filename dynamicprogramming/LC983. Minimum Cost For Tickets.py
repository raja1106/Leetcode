from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        table =[0 for i in range(len(days))]
        table[0] = min(costs)

        for i in range(1,len(days)):

            case1= table[i-1]+costs[0]

            j=i-1
            while (j>=0) and (days[j]>=days[i]-6):
                j -=1
            if(j>=0):
                case2=table[j]+costs[1]
            else:
                case2=costs[1]
            j=i-1
            while(j>=0) and (days[j]>=days[i]-29):
                j -=1
            if j>=0:
                case3=table[j]+costs[2]
            else:
                case3=costs[2]
            table[i]=min(case1,case2,case3)
        return table[-1]