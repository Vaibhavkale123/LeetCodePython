class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        print(nums)
        return k + 1
        # s1=set()
        # for i in nums:
        #     if i not in s1:
        #         s1.add(i)
        # n=list(s1)
        # for i in range(len(n),len(nums)):
        #     n.append('_')
        # nums=n
        # print(nums)
        # return len(s1)

s=Solution()
li=[1,1,2]
# li=[0,0,1,1,1,2,2,3,3,4]


print(s.removeDuplicates(li))