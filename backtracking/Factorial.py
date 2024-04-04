class Solution:
    def fact(self,n):
        result = 1

        for i in range(1,n+1):
            result *= i

        return result

    def fact_rec(self,n):
        if n == 1 or n== 0:
            return 1
        return n*self.fact_rec(n-1)



obj=Solution()
print(obj.fact(0))
print(obj.fact_rec(0))