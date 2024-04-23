class Solution:
    def fib(self, n: int) -> int:
        n1=0
        n2=1
        sum=0

        if n<=1:
            return 0 
        for i in range(1,n):
            sum=n1+n2
            n1=n2
            n2=sum
        return sum

        # better solution
    


s=Solution()
print(s.fib(2))
print(s.fib(3))
