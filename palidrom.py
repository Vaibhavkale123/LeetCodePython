class Solution:
    def isPalindrome(self, x: int) -> bool:
        # n=x
        # rev=0
        # while n!=0:
        #     rem=n%10
        #     rev=rev*10+rem
        #     n//=10
        
        # return rev==x
        # better solution
        return str(x)==str(x)[::-1]

s=Solution()
print(s.isPalindrome(-121))
print(s.isPalindrome(121))
