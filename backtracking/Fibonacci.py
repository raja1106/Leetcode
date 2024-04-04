class Solution:

    def fib(self,n):
        if n ==0 or n==1:
            return 1
        return self.fib(n-1)+self.fib(n-2)

obj=Solution()
print(obj.fib(5))