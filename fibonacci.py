class Solution:
    def fib(self, n: int) -> int:
        n1=0
        n2=1
        sum=0
        # if n==2:
        #     return n1+n2
        for i in range(n):
            sum+=n1+n2
            n1=n2
            n2=i
        return sum

        # better solution
    


s=Solution()
print(s.fib(2))