# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n_len = len(nums)
        l,r = 0,n_len-1
        while l <=r:
            m = (l + r)//2
            if nums[m] == m :
                l = m + 1
            else:
                r = m -1
        return l
